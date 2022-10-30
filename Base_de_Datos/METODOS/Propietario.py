class Propietario:


    Nombre = ""
    Direccion = ""
    Contacto = ""

    def __init__(self, Nombre, Direccion, Contacto):
        self.Nombre = Nombre,
        self.Direccion = Direccion,
        self.Contacto = Contacto

    def get_Nombre(self):
        return Nombre

    def set_Nombre(self, Nombre):
        self.Nombre = Nombre

    def get_Direccion(self):
        return Direccion

    def set_Direccion(self, Direccion):
        self.Direccion = Direccion

    def get_Contacto(self):
        return Contacto

    def set_Contacto(self, Contacto):
        self.Contacto = Contacto
        

    def _str(self):
        print('Nombre'+self.Propietario)
        print('Direccion'+self.Propietario)
        print ('Contacto'+self.Propietario)

    
