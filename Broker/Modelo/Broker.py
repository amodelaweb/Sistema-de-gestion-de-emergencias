import sys
import json
import os
sys.path.insert(1, os.path.join(sys.path[0], '../..'))
from Broker.Interfaz.Conection import Conection
from shared.Message import MessageType, Message, Message_Broker

class Broker(object):

    def __init__(self, ip, port, is_server, broadcast, balanceador_ip = "127.0.0.1"):
        super(Broker, self).__init__()
        self.ip = ip
        self.port = port
        self.suscribers = []
        self.publishers = []
        self.balanceador_ip = balanceador_ip
        self.temas = []
        self.brokers = []
        self.broadcast = broadcast
        self.is_server = is_server
        self.conection = Conection(self.ip, self.port)

    def __repr__(self):
        res = " ip " + self.ip + "port" + str(self.port)
        return res

    def add_client(self, cliente):
        print("===================== MI NUEVO CLIENTE ==============================")
        print(cliente)
        print("===================================================")
        self.suscribers.append(cliente)

    def add_publisher(self, publisher):
        print("======================== MI NUEVO PUBLISHER ===========================")
        print(publisher)
        print("===================================================")
        self.publishers.append(publisher)

    def add_broker(self, broker):
        print("================= MI NUEVO BROKER ==================================")
        print(broker)
        print("===================================================")
        self.brokers.append(broker)

    def send_info_broadcast(self , data):
        self.conection.send_data(self.port,self.broadcast,data)

    def broadcast_to_clients(self, data):
        print("============= BROADCAST A MIS CLIENTES ======================================")
        if not self.is_Registered(data.get('body').get('author')):
            print("------------------ No registrado")
            print("===================================================")
            return None
        for client in self.suscribers :
            for element in client.temas :
                print(element)
                if element in data.get('body').get('temas'):
                    self.conection.send_data(client.puerto, client.ip , data)
                    break
                #Fi
            #Rof
        print("=================================================== FIN DE BROADCAST CLIENTES")
        #Rof
    def boadcast_brokers(self, data):
        print("=================== FUI ELEJIDO PARA BROADCAST A BROKERS ================================")
        for broker in self.brokers :
            self.conection.send_data(broker.port, broker.ip , data)
        print("======================================================================== FIN DEL BROADCAST")
        #Rof
    def subscribe(self,ip_broker, port_broker):
        new_broker = Message_Broker(self.ip, self.port, self.broadcast)
        msg = Message(MessageType.BROKER, json.loads(new_broker.to_json()))
        self.conection.send_data(port=int(port_broker),  ip=ip_broker, data=msg.to_json())

    def is_Registered(self, name):
        for pub in self.publishers :
            if pub.nombre == name:
                return True
            #fi
        #rof
        return False

    def is_my_friend(self,  ip_broker):
        for brok in self.brokers :
            if brok.ip == ip_broker:
                return True
            #fi
        #rof
        return False

    def add_new_brokers(self, res):
        print("========= MIS NUEVOS BROKERS ======================")
        print(res.get('body'))
        print("===================================================")
        for bro in res.get('body'):
            self.brokers.append(Broker(bro.get('ip'),
                                       int(bro.get('port')) ,
                                       True,
                                       '255.255.255.255'))
