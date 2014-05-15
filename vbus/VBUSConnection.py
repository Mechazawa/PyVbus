import ssl
import socket
from .VBUSResponse import VBUSResponse


class VBUSAuthenticationException(Exception):
    def __init__(self, *args):
        super.__init__(*args)


class VBUSConnection(object):
    def __init__(self, host, port=7053, password=""):
        assert isinstance(port, int)
        assert isinstance(host, str)
        assert isinstance(password, str)
        self.host = host
        self.port = port
        self.password = password or False

        self._sock = None
        self._buffer = []

    def connect(self, sslsock=False):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if sslsock:
            self._sock = ssl.wrap_socket(self._sock)
        self._sock.connect((self.host, self.port))
        assert VBUSResponse(self._lrecv()).type == "HELLO"

        if self.password:
            self._lsend("PASS %s" % self.password)
            resp = VBUSResponse(self._lrecv())
            if not resp.positive:
                raise VBUSAuthenticationException("Could not authenticate: %s" % resp.message)

    def _lrecv(self):
        c, s = '', ''
        while c != '\n':
            c = self._sock.recv(1)
            if c == '':
                break
            s += c
        return s.strip('\r\n')

    def _lsend(self, s):
        self._sock.send(s + "\r\n")


