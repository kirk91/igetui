# encoding: utf-8

import base64
import hashlib
import time
import uuid

import requests

from .exc import RequestException


class IGeTui(object):

    def __init__(self, host, app_key, master_secret):
        self.app_key = app_key
        self.master_secret = master_secret
        self.host = host

    def push_message_to_single(self, message, target, request_id=None):
        if request_id is None:
            request_id = str(uuid.uuid1())

        transparent = message.data.get_transparent()
        params = {
            'requestId': request_id,
            'action': 'pushMessageToSingleAction',
            'appkey': self.app_key,
            'clientData': base64.encodestring(transparent.SerializeToString()),
            'transmissionContent': message.data.content,
            'isOffline': message.is_offline,
            'offlineExpireTime': message.offline_expire_time,
            'pushNetWorkType': message.push_network_type,
            'appId': target.app_id,
            'clientId': target.client_id,
            'alias': target.alias,
            'type': 2,
            'pushType': message.data.push_type,
        }

        return self._send(params)

    def _gen_sign(self, timestamp):
        val = self.app_key + str(timestamp) + self.master_secret
        return hashlib.md5(val.encode()).hexdigest()

    def _connect(self):
        timestamp = int(time.time() * 1000)
        sign = self._gen_sign(timestamp)
        params = dict()
        params['action'] = 'connect'
        params['appkey'] = self.app_key
        params['timeStamp'] = timestamp
        params['sign'] = sign

        ret = self._post(params)
        if 'success' == ret.get('result'):
            return True
        raise Exception("app_key or master_secret is auth failed.")

    def _send_message(self, params):
        if params['request_id'] is None:
            params['request_id'] = str(uuid.uuid1())
        request_id = params['request_id']

        ret = self._post(params)
        if ret is None or ret == '':
            raise RequestException(request_id, 'request failed')

        if 'sign_error' == ret.get('result'):
            if self._connect():
                ret = self._post(params)
        return ret

    def _post(self, params):
        headers = {
            'Gt-Action': params.get('action')
        }

        try:
            rep = requests.post(self.host, json=params, headers=headers)
        except Exception as e:
            raise e

        if not rep.ok:
            return None

        try:
            data = rep.json()
        except ValueError as e:
            return None
        return data
