import mysql.connector
    
try: 
    conexion = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    passwd = "root",
    database = "Bd_Inmobiliaria"
    )
        
    if conexion.is_connected():
        print("LA CONEXION FUE EXITOSA")

        info = conexion.get_server_info()
        print("LA INFORMACION DEL SERVIDOR ES:",info)
except: 
    print("¡FALLO LA CONEXION")



cursor=conexion.cursor()

consulta = "insert into Propiedad (Id_Propiedad, Id_Tipo, Id_Estado, Id_Operacion_Comercial, Id_Propietario, Nombre, Direccion, Contacto) values (01,5,600,2,1,'Andres Montaño','San Luis 23',29956);"
cursor.execute(consulta)

conexion.commit()
conexion.close()
