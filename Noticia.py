import json import *
import datatime

class Noticia(JSONEncoder):
    """A class that represents a news, this is the message that will be sent
       by the source and received by the client."""
    def __init__(self, body='', author='', timestamp=datetime.datetime.utcnow(), json=None):
        self.body = body
        self.author = author
        self.timestamp = timestamp
        if json is not None:
            self.__initializar_with_json(json)

    def __initializar_with_json(self, json):
        json_obj = json.loads(json)
        self.body = json_obj.get('body')
        self.author = json_obj.get('author')
        self.timestamp = json_obj.get('timestamp')
