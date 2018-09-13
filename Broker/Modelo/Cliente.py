class Cliente():

    # CONSTRUCTOR
    def __init__(self, ip, puerto, nombre, residencia, profesion, comp_familiar, temas):
        super(Cliente, self).__init__()
        self.ip = ip
        self.puerto = puerto
        self.nombre = nombre
        self.residencia = residencia
        self.comp_familiar = comp_familiar
        self.temas = temas

    def __repr__(self):
        res = "* Nombre " + self.nombre + " *residencia " + self.residencia + " *comp_familiar " + str(self.comp_familiar) + " *temas " + str(self.temas) + " ip " + self.ip
        return res
