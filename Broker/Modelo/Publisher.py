class Publisher:
    def __init__(self, ip, nombre):
        self.ip = ip
        self.nombre = nombre

    def __repr__(self):
        res = "* Nombre " + self.nombre + " ip " + self.ip
        return res
