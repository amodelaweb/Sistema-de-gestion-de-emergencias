from json import JSONEncoder
class NewsCategory(JSONEncoder):
    INUNDACIONES = 1
    VENDAVALES = 2
    INCENDIOS = 3
    DERRUMBES = 4

    def default(self):
        return self.__dict__
