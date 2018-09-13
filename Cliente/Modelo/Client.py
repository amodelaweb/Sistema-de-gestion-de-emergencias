import sys
import os
import json

sys.path.insert(1, os.path.join(sys.path[0], '../..'))
from shared.Message import Message, MessageType
from shared.NewsCategory import NewsCategory
from shared.Connection import Connection

class Client(json.JSONEncoder):
    """Class that represents a client, a client can subscribe to the broker to
    receive news"""

    def default(self):
        return self.__dict__

    def __init__(self, nombre, residencia, profesion, ip_broker, port_broker, ip='127.0.0.1', puerto=5001, comp_familiar=[], temas = []):
        self.ip = ip
        self.puerto = puerto
        self.nombre = nombre
        self.residencia = residencia
        self.comp_familiar = comp_familiar
        self.temas = temas
        self.ip_broker = ip_broker
        self.port_broker = port_broker

    def to_json(self):
        return json.dumps(self.__dict__)

    def subscribe(self):
        msg = Message(MessageType.SUBSCRIBER, json.loads(self.to_json()))
        conn = Connection()
        conn.send_data(port=self.port_broker,  ip=self.ip_broker, data=msg.to_json())
"""
c = Client(nombre='Juan Pablo',
           residencia='Calle 61 No. 4-66',
           profesion='Ingeniero',
           comp_familiar=[1,2,3],
           temas=[NewsCategory.INUNDACIONES, NewsCategory.INCENDIOS],
           ip_broker='192.168.0.113',
           port_broker=5001
)

c.subscribe()
"""
