# encoding: utf-8


class RequestException(Exception):
    def __init__(self, request_id, message):
        self.request_id = request_id
        self.message = message

    def __str__(self):
        return self.message

    def get_request_id(self):
        return self.request_id
