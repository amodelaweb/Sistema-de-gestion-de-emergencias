import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../..'))
from Cliente.Modelo.Client import Client

class ClientMainViewController:
    def __init__(self, clientMainView):
        self.clientMainView = clientMainView

    def subscribePushButtonHandler(self):
        broker_data = self.clientMainView.getBrokerData()
        user_data = self.clientMainView.getUserData()
        temas = []
        i = 1
        for isMarked in user_data['temas']:
            if isMarked:
                temas.append(i)
            i += 1
        self.client = Client(
            nombre=user_data['nombre'],
            residencia=user_data['residencia'],
            ip_broker=broker_data['ip_broker'],
            port_broker=broker_data['port_broker'],
            ip=user_data['ip'],
            puerto=user_data['puerto'],
            comp_familiar=user_data['comp_familiar'],
            temas=temas
        )
        self.client.subscribe()


