class Conection():

    def __init__(ip, port):
        super(Conection, self).__init__()
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    def listen(self, port , buffer_size):
        sock.bind(("", port))
        data, addr = self.sock.recvfrom(buffer_size)
        self.sock.shutdown(socket.SOCK_DGRAM)
        json_obj = json.loads(data)
        return json_obj

    def send_data (self, port, ip , data):
        mensaje = str(data).replace("'",'"')
        mensaje = mensaje.encode('utf-8')
        try:
            self.sock.sendto(mensaje,(ip, port))
            return true
        except Exception as e:
            print(e)
            return false
