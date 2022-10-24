class Estado:


    Nombre_Estado = ""

    def __init__(self, Nombre_Estado):
        self.Nombre_Estado = Nombre_Estado,

    def get_Nombre_Estado(self):
        return Nombre_Estado

    def set_Nombre_Estado(self, Nombre_Estado):
        self.Nombre_Estado = Nombre_Estado

    def _str(self):
        print('Nombre_Estado'+self.Nombre_Estado)

    
