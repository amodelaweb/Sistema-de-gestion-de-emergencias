import os
import sys
import threading

# 192.168.0.27

sys.path.insert(1, os.path.join(sys.path[0], '../..'))
from Publicador.Modelo.Publisher import Publisher
from shared.Noticia import Noticia
from shared.NewsCategory import NewsCategory


class MainWindowController:
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow

    def connectPushButtonHandler(self):
        broker_data = self.mainWindow.getBrokerData()
        self.publisher = Publisher(ip_broker=broker_data['ip_broker'],
                                   nombre=broker_data['nombre'],
                                   port_broker=broker_data['port_broker'])
        self.publisher.subscribe()
        self.mainWindow.stateLabel.setText('Conectado')

    def sendPushButtonHandler(self):
        if self.publisher is None:
            raise ValueError('You have not connected a publisher')
        news_data = self.mainWindow.getNewsData()
        temas = []
        i = 1
        for isMarked in news_data['temas']:
            if isMarked:
                temas.append(i)
            i+=1
        news = Noticia(body=news_data['body'], author=news_data['author'], temas=temas)
        self.publisher.send_news(news)

    def loadJsonPushButtonHandler(self):
        path = self.mainWindow.getFilePath()
        print('From Controller', path)
        self.publisher.read_file(path)
        self.publisher.send_packages_at_time()
        hilo_match = threading.Thread(target=self.publisher.send_packages_at_time ) # TODO - Fix thread for the UI not to froze
        hilo_match.start()