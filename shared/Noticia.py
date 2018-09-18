import json
import os
import sys
import datetime

sys.path.insert(1, os.path.join(sys.path[0], '../..'))
from shared.NewsCategory import NewsCategory

class Noticia:
    """A class that represents a news, this is the message that will be sent
       by the source and received by the client."""
    def __init__(self, body='', author='', temas=[], timestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), json=None):
        self.body = body
        self.author = author
        self.timestamp = timestamp
        self.temas = temas;
        if json is not None:
            self.__initializar_with_json(json)

    def __initializar_with_json(self, json):
        json_obj = json.loads(json)
        self.body = json_obj.get('body')
        self.author = json_obj.get('author')
        self.timestamp = json_obj.get('timestamp')
        self.temas = json_obj.get('temas')

    def to_json(self):
        return json.dumps(self.__dict__)

    def to_string(self):
        author = 'Autor: ' + self.author
        cuerpo = 'Noticia: ' + self.body
        hora = 'Timestamp: ' +self.timestamp

        temas = ''
        for i in self.temas:
            if i == NewsCategory.DERRUMBES:
                temas += 'Derrumes '
            if i == NewsCategory.INCENDIOS:
                temas += 'Incedios '
            if i == NewsCategory.INUNDACIONES:
                temas += 'Inundaciones '
            if i == NewsCategory.VENDAVALES:
                temas += 'Vendabales '
        return author + ' ' + cuerpo + ' ' + temas + ' ' + hora
