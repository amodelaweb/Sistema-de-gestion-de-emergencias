import sys
import os

sys.path.insert(1, os.path.join(sys.path[0], '../..'))
from shared.Noticia import Noticia
from shared.Connection import Connection

class Publisher:
    """This class is goning to send news to the broker."""
    def __init__(self, ip='127.0.0.1', port=5001, brokerIp, brokerPort=5001):
        self.ip = ip
        self.port = port
        self.brokerPort = brokerPort
        self.brokerIp = brokerIp

    def send_news(self, news):
        conn = Conection();
        conn.send_data(port=self.brokerPort,  ip=self.brokerIp, data=news.to_json())

news = Noticia(body='Test Body', author='El Tiempo')
p = Publisher(brokerIp='192.168.0.113', brokerPort=5001)
p.send_news(news)
