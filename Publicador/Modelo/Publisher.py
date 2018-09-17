import sys
import os
import json
import datetime
import threading

sys.path.insert(1, os.path.join(sys.path[0], '../..'))
from shared.Message import Message, MessageType
from shared.Noticia import Noticia
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
        self.cola_eventos = []

    def send_news(self, news):
        msg = Message(MessageType.NEWS, json.loads(news.to_json()))
        conn = Connection(self.ip, self.port);
        conn.send_data(port=self.port_broker,  ip=self.ip_broker, data=msg.to_json())

    def to_json(self):
        return json.dumps(self.__dict__)

    def subscribe(self):
        msg = Message(MessageType.PUBLISHER, json.loads(self.to_json()))
        conn = Connection(self.ip, self.port)
        conn.send_data(port=self.port_broker,  ip=self.ip_broker, data=msg.to_json())

    def read_file (self, file_name):
        jsonOb = json.loads(open(file_name).read())
        print(jsonOb)
        array = jsonOb.get('mensajes')
        orderkey = lambda x: x.get('timestamp')
        self.cola_eventos.extend(array)
        self.cola_eventos.sort(key=orderkey)
        #self.send_packages_at_time()
        #hilo_match = threading.Thread(target=self.send_packages_at_time )
        #hilo_match.start()

    def send_packages_at_time(self):
        print(len(self.cola_eventos))
        while(self.cola_eventos):
            time = datetime.datetime.strptime(self.cola_eventos[0].get('timestamp'), "%Y-%m-%d %H:%M:%S")
            result = time.timestamp() - datetime.datetime.now().timestamp()
            if(result <= 0):
                #print("In array " , time.strftime("%Y-%m-%d %H:%M:%S") , " In Now " ,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") , " result " , result )
                print("Envie el paquete")
                self.send_news(Noticia(body=self.cola_eventos[0].get('body'),
                                       author=self.cola_eventos[0].get('author'),
                                       temas=self.cola_eventos[0].get('temas')))
                self.cola_eventos.pop(0)

#news = Noticia(body='Test Body',
                #author='El Tiempo',
                #temas=[NewsCategory.INCENDIOS, NewsCategory.DERRUMBES])
#p = Publisher(ip_broker='192.168.0.27', port_broker=5001, nombre='El Tiempo')
#p.subscribe()
#p.send_news(news)
#script_dir = os.path.dirname(__file__)
#rel_path = 'file.json'
#p.read_file(os.path.join(script_dir, rel_path))
#p.send_packages_at_time()
#hilo_match = threading.Thread(target=p.send_packages_at_time )
#hilo_match.start()
#while True:
#    pass
