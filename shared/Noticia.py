import json
import datetime

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
