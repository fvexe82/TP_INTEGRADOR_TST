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

consulta = "UPDATE Propiedad SET Nombre = 'Juan Carlos'  WHERE Id_Propiedad = 01;"

cursor.execute(consulta)

conexion.commit()
conexion.close()