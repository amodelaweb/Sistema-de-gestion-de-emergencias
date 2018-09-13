import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from Interfaz.Conection import Conection
from Modelo.Cliente import Cliente
from Modelo.Publicador import Publicador

class Broker(object):

    def __init__(self, ip, port, ):
        super(Broker, self).__init__()
        self.ip = ip
        self.port = port
        self.suscribers = []
        self.publishers = []
        self.conection = Conection(self.ip, self.port)
