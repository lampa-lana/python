import pytest
import socket as s
from my_chat.server2 import Server


@pytest.fixture
def socket(request):
    _socket = s.socket(s.AF_INET, s.SOCK_DGRAM)

    def socket_teardown():
        _socket.close()
    request.addfinalizer(socket_teardown)
    return _socket


def test_server_connect(socket):
    socket.bind(('localhost', 9100))
    assert socket


@pytest.yield_fixture
def socket():
    _socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    yield _socket
    _socket.close()
