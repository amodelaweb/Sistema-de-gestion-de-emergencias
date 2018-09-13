import sys
import os

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from Noticia import Noticia

class Publisher:
    """This class is goning to send news to the broker."""
    def __init__(self, ip, port, broker=None):
        self.ip = ip
        self.port = port
        self.broker = broker

    def send_news(self):
        news = Noticia(body='Test Body', author='El Tiempo')

    def imprimir(self):
        print(self.ip);
        print(self.port);

print('Hello World')
