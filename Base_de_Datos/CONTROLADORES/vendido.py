from Conexion import conexion


def vendido(self):
    cursor=conexion.cursor()
    cursor.execute("SELECT Nombre_Estado, Nombre_Tipo, P.Nombre, P.Direccion, P.Contacto FROM  Propiedad Pr inner join Estado E on  Pr.Id_Estado=E.Id_Estado inner join Propietario P on Pr.Id_Propietario=P.Id_Propietario inner join Tipo T on Pr.Id_Tipo=T.Id_Tipo where Nombre_Estado like 'Vendid%';")
    for x in cursor:
        print(x)
    conexion.close()
    print("CONEXION CERRADA EXITOSAMENTE")



