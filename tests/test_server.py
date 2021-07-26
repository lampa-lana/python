from unittest.mock import patch, Mock
from socket import socket
import unittest
import socket
import time
from my_chat.server2 import Server


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
        self.assertIsInstance(self.result, int)
        print(self.result)

    def tearDown(self):
        print('end')


class TestServerQuit(unittest.TestCase):
    @patch('my_chat.server2.Server')
    def setUp(self, result):
        self.result = Server.get_quit(self)
        print('start')

    def test_port(self):
        self.assertFalse(self.result)
        print(self.result)

    def tearDown(self):
        print('end')


class TestServerSend(unittest.TestCase):
    @patch('my_chat.server2.Server')
    def setUp(self, result):
        self.result = Server.get_quit(self)
        print('start')

    def test_port(self):
        self.assertFalse(self.result)
        print(self.result)

    def tearDown(self):
        print('end')


if __name__ == '__main__':
    unittest.main()


#python -m tests.test_server
