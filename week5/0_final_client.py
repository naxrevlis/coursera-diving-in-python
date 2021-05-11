import socket


class Client():
    def __init__(self, addr, port, timeout=None):
        self.addr = addr
        self.port = port
        self.timeout = timeout

        self.sock = socket.socket()
        self.sock.connect((self.addr, self.port))
        self.sock.listen(socket.SOMAXCONN)

    def put(self, metric, value, timestamp):
        self.sock.sendall(metric+" "+str(value)+" "+str(timestamp)+"\n")

    def get(self,metric):
        self.sock.sendall(metric+"\n")