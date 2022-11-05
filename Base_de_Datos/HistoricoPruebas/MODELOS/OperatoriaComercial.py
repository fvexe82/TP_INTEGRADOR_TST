class OperatoriaComercial:


    Nombre_Operatoria_Comercial = ""

    def __init__(self, Nombre_Operatoria_Comercial):
        self.Nombre_Operatoria_Comercial = Nombre_Operatoria_Comercial,

    def get_Nombre_Operatoria_Comercial(self):
        return Nombre_Operatoria_Comercial

    def set_Nombre_Operatoria_Comercial(self, Nombre_Operatoria_Comercial):
        self.Nombre_Operatoria_Comercial = Nombre_Operatoria_Comercial

    def _str(self):
        print('Nombre_Operatoria_Comercial'+self.Nombre_Operatoria_Comercial)

    
