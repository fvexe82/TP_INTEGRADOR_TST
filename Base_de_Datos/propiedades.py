import mysql.connector

class propiedades:

    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost", user="root",passwd="maytecarolina",
        database="Bd_Inmobiliaria")

    def __str__(self):
        datos=self.consulta_propiedades()
        aux=""
        for row in datos:
            aux = aux + str (row) + "\n"
        return aux
    
    def consulta_propiedades(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * from Propiedad")
        datos = cur.fetchall()
        cur.close()
        return datos
    
    def buscar_propiedades(self, Id_Estado):
        cur = self.cnn.cursor()
        sql = "SELECT * FROM Propiedad WERE Id_Estado = {}".format(Id_Estado)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()
        return datos
    
    def listarPropiedades(self):
        cur=self.cnn.cursor()
        sql = "SELECT Nombre_Estado, Nombre_Tipo, P.Nombre, P.Direccion, P.Contacto, Pr.Nombre, Pr.Direccion, Pr.Contacto FROM  Propiedad Pr inner join Estado E on  Pr.Id_Estado=E.Id_Estado inner join Propietario P on Pr.Id_Propietario=P.Id_Propietario inner join Tipo T on Pr.Id_Tipo=T.Id_Tipo"
        cur.execute(sql)
        datos=cur.fetchone()
        cur.close()
        return datos
    
    def inserta_propiedad(self,Id_Tipo,Id_Estado,Id_Operatoria_Comercial,Id_Propietario,Nombre,Direccion,Contacto):
        cur = self.cnn.cursor()
        sql = '''INSERT INTO Propiedad (Id_Tipo,Id_Estado,Id_Operacion_Comercial,Id_Propietario,Nombre,Direccion,Contacto) VALUES ('{}','{}','{}','{}','{}','{}','{}')'''.format(Id_Tipo,Id_Estado,Id_Operatoria_Comercial,Id_Propietario,Nombre,Direccion,Contacto)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

    def elimina_propiedad(self,Id_Propiedad):
        cur = self.cnn.cursor()
        sql = '''DELETE FROM Propiedad WHERE Id_Propiedad = {}'''.format(Id_Propiedad)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()
        cur.close()
        return n
     
    def modifica_propiedad(self,Id_Propiedad,Id_Tipo,Id_Estado,Id_Operatoria_Comercial,Id_Propietario,Nombre,Direccion,Contacto):
        cur = self.cnn.cursor()
        sql = '''UPDATE Propiedad SET Id_Tipo='{}', Id_Estado='{}',Id_Operacion_Comercial='{}',Id_Propietario='{}',Nombre='{}',Direccion='{}',Contacto='{}' WHERE Id_Propiedad={}'''.format(Id_Tipo,Id_Estado,Id_Operatoria_Comercial,Id_Propietario,Nombre,Direccion,Contacto)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

