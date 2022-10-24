class Tipo:


    Nombre_Tipo = ""

    def __init__(self, Nombre_Tipo):
        self.Nombre_Tipo = Nombre_Tipo,

    def get_Nombre_Tipo(self):
        return Nombre_Tipo

    def set_Nombre_Tipo(self, Nombre_Tipo):
        self.Nombre_Tipo = Nombre_Tipo

    def _str(self):
        print('Nombre_Tipo'+self.Nombre_Tipo)

    
