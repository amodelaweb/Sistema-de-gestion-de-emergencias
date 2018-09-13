from socket import *
import json

class Conection():
    # CONSTRUCTOR
    def __init__(self, ip, port):
        super(Conection, self).__init__()
        self.ip = ip
        self.port = port
        self.sock = socket(AF_INET,SOCK_DGRAM)
    # METODOS DEL SERVIDOR
    def init_server(self):
        self.sock.bind(("", self.port))

    def close_socket(self):
        self.sock.close()

    def listen(self, buffer_size):
        #self.sock.close()
        data, addr = self.sock.recvfrom(buffer_size)
        json_obj = json.loads(data)
        return json_obj, addr
    # METODOS DE ENVIO
    def send_data (self, port, ip , data):
        mensaje = str(data).replace("'",'"')
        mensaje = mensaje.encode('utf-8')
        try:
            print("Voy a enviar")
            print(mensaje)
            print("...................")
            print("IP " + ip + " . port . " + str(port) )
            self.sock.sendto(mensaje,(ip, port))
            return True
        except Exception as e:
            print(e)
            return False
