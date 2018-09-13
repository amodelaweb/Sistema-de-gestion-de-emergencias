import socket
import json
 
class Connection():
    # CONSTRUCTOR
    def __init__(self, ip='127.0.0.1', port=5001):
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # METODOS DEL SERVIDOR
    def init_server(self):
        self.sock.bind(("", self.port))

    def close_socket(self):
        self.sock.close()

    def listen(self, buffer_size):
        #self.sock.close()
        data, addr = self.sock.recvfrom(buffer_size)
        json_obj = json.loads(data)
        return json_obj

    # METODOS DE ENVIO
    def send_data (self, port, ip , data):
        mensaje = str(data).replace("'",'"')
        mensaje = mensaje.encode('utf-8')
        try:
            self.sock.sendto(mensaje,(ip, port))
            return True
        except Exception as e:
            print(e)
            return False
