from ... import Noticia

class Publisher:
    """This class is goning to send news to the broker."""
    def __init__(self, ip, port, broker):
        self.ip = ip
        self.port = port
        self.broker = broker

    def send_news(self):
        news = Noticia(body='Test Body', author='El Tiempo')
