from socket import socket
import unittest
import socket
import time
from my_chat.server2 import Server
from unittest.mock import patch, Mock


class TestServerHost(unittest.TestCase):
    @patch('my_chat.server2.Server')
    def setUp(self, result):
        self.result = Server.get_host(self)
        print('start')

    def test_host(self):
        self.assertIsNotNone(self.result)
        print(self.result)

    def tearDown(self):
        print('end')


class TestServerPort(unittest.TestCase):
    @patch('my_chat.server2.Server')
    def setUp(self, result):
        self.result = Server.get_port(self)
        print('start')

    def test_port(self):
        result = Server.get_port(self)
        self.assertIsInstance(result, int)
        print(result)

    def tearDown(self):
        print('end')


if __name__ == '__main__':
    unittest.main()
