import sys
import json
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from Interfaz.Conection import Conection
sys.path.insert(1, os.path.join(sys.path[0], '../..'))
from shared.Message import MessageType, Message, Message_Broker

class Balanceador:
    """docstring for Balanceador."""
    def __init__(self, ip , port):
        super(Balanceador, self).__init__()
        self.ip = ip
        self.port = port
        self.brokers = []
        self.contador = 0
        self.numbrokers = 0
        self.conection = Conection(self.ip, self.port)

    def add_broker(self, broker):
        print(broker)
        self.numbrokers = self.numbrokers + 1
        self.brokers.append(broker)

    def round_robin(self, message):
        if self.numbrokers > 0:
            band = True
            inicial = self.contador % self.numbrokers
            contador_i = self.contador
            while band :
                print("====================== PING AL ELEGIDO =============================")
                indexsel = self.contador % self.numbrokers
                hostname = self.brokers[indexsel].ip
                response = os.system("ping -c 1 " + hostname)
                self.contador = self.contador + 1
                if response == 0:
                    print ('is up!')
                    print ("===============================")
                    print ("ENVIE AL INDEX ", indexsel)
                    print ("===============================")
                    self.conection.send_data(self.brokers[indexsel].port, self.brokers[indexsel].ip , message)
                    band = False
                else :
                    print ("========= CAMBIE DE HOST !!======================")
                    print ('is down! ', hostname )
                    print ("============== OK OK OK OK =================")
                    if inicial == indexsel and contador_i != self.contador-1:
                        band = False

    def send_brokers(self, ip_broker , port_broker):
        temp = []
        for bro in self.brokers:
            new_broker = Message_Broker(bro.ip, bro.port, bro.broadcast)
            temp.append(json.loads(new_broker.to_json()))

        msg = Message(MessageType.GET_BROKERS, temp)
        self.conection.send_data(port=int(port_broker),  ip=ip_broker, data=msg.to_json())
