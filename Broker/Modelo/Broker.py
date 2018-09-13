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
        self.Brokers = []
        self.temas = []
        self.brokers = []
        self.broadcast = broadcast
        self.is_server = is_server
        self.conection = Conection(self.ip, self.port)

    def __repr__(self):
        res = " ip " + self.ip + "port" + self.port
        return res

    def add_client(self, cliente):
        print(cliente)
        self.suscribers.append(cliente)

    def add_publisher(self, publisher):
        print(publisher)
        self.publishers.append(publisher)

    def add_broker(self, broker):
        print(broker)
        self.brokers.append(broker)

    def send_info_broadcast(self , data):
        self.conection.send_data(self.port,self.broadcast,data)

    def broadcast_to_clients(self, data):

        for client in self.suscribers :
            for element in client.temas :
                print(element)
                if element in data.get('body').get('temas'):
                    print("-----------------")
                    print(client.puerto , " - " , client.ip)
                    print("-----------------")
                    self.conection.send_data(client.puerto, client.ip , data)
                    #break
                #Fi
            #Rof
        #Rof
