import psutil


class Interface:
    def __init__(self):
        self._index = 0
        self._name = ""
        self._bytes_sent = 0
        self._bytes_received = 0

    def set_index(self, index):
        self._index = index

    def set_name(self, name):
        self._name = name

    def set_bytes_sent(self, bytes_sent):
        self._bytes_sent = bytes_sent

    def set_bytes_received(self, bytes_received):
        self._bytes_received = bytes_received

    def get_index(self):
        return self._index

    def get_name(self):
        return self._name

    def get_bytes_sent(self):
        return self._bytes_sent

    def get_bytes_received(self):
        return self._bytes_received
