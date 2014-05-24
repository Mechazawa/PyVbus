import ssl
import socket
from .VBUSResponse import VBUSResponse
from .util import hexdump


MODE_COMMAND = 0
MODE_DATA = 1


class VBUSException(Exception):
    def __init__(self, *args):
        super.__init__(*args)



class VBUSConnection(object):
    def __init__(self, host, port=7053, password="", verbose=False):
        assert isinstance(port, int)
        assert isinstance(host, str)
        assert isinstance(password, str)
        assert isinstance(verbose, bool)
        self.host = host
        self.port = port
        self.password = password or False
        self.verbose = verbose

        self._mode = MODE_COMMAND
        self._sock = None
        self._buffer = []

    def connect(self, sslsock=False):
        assert not self._sock
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if sslsock:  # Unlikely that we'll ever connect to the VBUS using an ssl socket but "why not?"
            self._sock = ssl.wrap_socket(self._sock)
        self._sock.connect((self.host, self.port))
        assert VBUSResponse(self._lrecv()).type == "HELLO"
        if self.password:
            self.authenticate()

    def authenticate(self):
        assert self.password
        assert self._mode == MODE_COMMAND
        self._lsend("PASS %s" % self.password)
        resp = VBUSResponse(self._lrecv())
        if not resp.positive:
            raise VBUSException("Could not authenticate: %s" % resp.message)

    def data(self):
        assert self._sock
        if self._mode is not MODE_DATA:
            self._lsend("DATA")

            resp = VBUSResponse(self._lrecv())
            if not resp.positive:
                raise VBUSException("Could create a data stream: %s" % resp.message)
            self._mode = MODE_DATA
        return self._brecv()

    def getmode(self):
        return self._mode

    def _lrecv(self):
        c, s = '', ''
        while c != '\n':
            c = self._sock.recv(1)
            if c == '':
                break
            s += c
        s = s.strip('\r\n')
        if self.verbose:
            print "< " + s
        return s

    def _brecv(self, n=1024):
        d = self._sock.recv(n)
        if self.verbose:
            print hexdump(d)
        return d

    def _lsend(self, s):
        if self.verbose:
            print "> " + s
        self._sock.send(s + "\r\n")

    def _bsend(self, s):
        self._sock.send(s)


