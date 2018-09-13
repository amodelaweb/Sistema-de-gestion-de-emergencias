import json
import datetime

from enum import Enum

class MessageType(json.JSONEncoder):
    PUBLISHER = 1
    SUBSCRIBER = 2
    BROKER = 3
    NEWS = 4

    def default(self):
        return self.__dict__

class Message:
    """Are the messages that are going to flow through the network"""

    def __init__(self, messageType, body):
        self.messageType = messageType
        self.body = body

    def to_json(self):
        return json.dumps(self.__dict__)
