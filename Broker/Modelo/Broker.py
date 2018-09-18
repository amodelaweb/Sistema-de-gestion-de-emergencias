import sys
import json
import os
sys.path.insert(1, os.path.join(sys.path[0], '../..'))
from Broker.Interfaz.Conection import Conection
from shared.Message import MessageType, Message, Message_Broker

class Broker(object):

    def __init__(self, ip, port, is_server, broadcast):
        super(Broker, self).__init__()
        self.ip = ip
        self.port = port
        self.suscribers = []
        self.publishers = []
        self.temas = []
        self.brokers = []
        self.broadcast = broadcast
        self.is_server = is_server
        self.conection = Conection(self.ip, self.port)

    def __repr__(self):
        res = " ip " + self.ip + "port" + str(self.port)
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
        print("al menos llego")
        if not self.is_Registered(data.get('body').get('author')):
            print("No registrado")
            return None
        for client in self.suscribers :
            for element in client.temas :
                print(element)
                if element in data.get('body').get('temas'):
                    self.conection.send_data(client.puerto, client.ip , data)
                    return None
                    #break
                #Fi
            #Rof
        #Rof
    def boadcast_brokers(self, data):
        for broker in self.brokers :
            self.conection.send_data(broker.port, broker.ip , data)
        #Rof
    def subscribe(self,ip_broker, port_broker):
        self.add_broker(Broker(ip_broker,port_broker, True, self.broadcast))
        new_broker = Message_Broker(self.ip, self.port, self.broadcast)
        msg = Message(MessageType.BROKER, json.loads(new_broker.to_json()))
        self.conection.send_data(port=int(port_broker),  ip=ip_broker, data=msg.to_json())

    def is_Registered(self, name):
        for pub in self.publishers :
            if pub.nombre == name:
                return True
        return False
