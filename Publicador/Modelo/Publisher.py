import sys
import os
import json

sys.path.insert(1, os.path.join(sys.path[0], '../..'))
from shared.Noticia import Noticia
from shared.Message import Message, MessageType
from shared.NewsCategory import NewsCategory
from shared.Connection import Connection

class Publisher:
    """This class is goning to send news to the broker."""
    def __init__(self, ip_broker, nombre, ip='127.0.0.1', port=5001, port_broker=5001):
        self.ip = ip
        self.port = port
        self.port_broker = port_broker
        self.ip_broker = ip_broker
        self.nombre = nombre

    def send_news(self, news):
        msg = Message(MessageType.NEWS, json.loads(news.to_json()))
        conn = Connection();
        conn.send_data(port=self.port_broker,  ip=self.ip_broker, data=msg.to_json())

    def to_json(self):
        return json.dumps(self.__dict__)

    def subscribe(self):
        msg = Message(MessageType.PUBLISHER, json.loads(self.to_json()))
        conn = Connection()
        conn.send_data(port=self.port_broker,  ip=self.ip_broker, data=msg.to_json())

news = Noticia(body='Test Body',
                author='El Tiempo',
                temas=[NewsCategory.INCENDIOS])
p = Publisher(ip_broker='192.168.0.113', port_broker=5001, nombre='El Tiempo')
# p.subscribe()
p.send_news(news)
