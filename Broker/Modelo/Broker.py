import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from Interfaz.Conection import Conection

class Broker(object):

    def __init__(self, ip, port, is_server, broadcast):
        super(Broker, self).__init__()
        self.ip = ip
        self.port = port
        self.suscribers = []
        self.publishers = []
        self.broadcast = broadcast
        self.is_server = is_server
        self.conection = Conection(self.ip, self.port)

    def add_client(self, cliente):
        self.suscribers.append(client)

    def add_publisher(self, publisher):
        self.publishers.append(publisher)

    def send_info_broadcast(self , data):
        self.conection.send_data(self.port,self.broadcast,data)

    def broadcast_to_clients(self, arg):
        pass
