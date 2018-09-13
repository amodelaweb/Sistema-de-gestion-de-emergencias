import sys
import os

sys.path.insert(1, os.path.join(sys.path[0], '../..'))
from Noticia import Noticia
from Broker.Interfaz.Conection import Conection

class Publisher:
    """This class is goning to send news to the broker."""
    def __init__(self, ip, port, brokerIp='127.0.0.1', brokerPort=5001):
        self.ip = ip
        self.port = port
        self.brokerPort = brokerPort
        self.brokerIp = brokerIp

    def send_news(self, news):
        conn = Conection('192.168.0.112', 5001);
        conn.send_data(port=self.brokerPort,  ip=self.brokerIp, data=news.to_json())

news = Noticia(body='Test Body', author='El Tiempo')
p = Publisher(ip='192.168.0.112', port=5001, brokerIp='192.168.0.113', brokerPort=5001)
p.send_news(news)
