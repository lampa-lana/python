from socket import socket
import unittest
import socket
import time
from my_chat.client1 import Client
from unittest.mock import patch, Mock


class TestClientHost(unittest.TestCase):
    @patch('my_chat.client1.Client')
    def setUp(self, result):
        self.result = Client.get_host_cl(self)
        print('start')

    def test_host(self):
        self.assertIsNotNone(self.result)
        print(self.result)

    def tearDown(self):
        print('end')


class TestClientPort(unittest.TestCase):
    @patch('my_chat.client1.Client')
    def setUp(self, result):
        self.result = Client.get_port_cl(self)
        print('start')

    def test_port(self):
        self.assertIsInstance(self.result, int)
        print(self.result)

    def tearDown(self):
        print('end')


if __name__ == '__main__':
    unittest.main()


# python -m tests.test_client
