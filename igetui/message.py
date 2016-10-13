# encoding: utf-8

from igetui import template


class Message(object):

    def __init__(self, data=None):
        if data is None:
            data = template.Base()
        self.is_offline = False
        self.data = data
        self.push_network_type = 0
        self.priority = 0

    @property
    def offline_expire_time(self, expire_time):
        self.offline_expire_time = expire_time
