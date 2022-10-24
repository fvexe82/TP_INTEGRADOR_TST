import mysql.connector
    
try: 
    conexion = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    passwd = "maytecarolina",
    database = "Bd_Inmobiliaria"
    )
        
    if conexion.is_connected():
        print("LA CONEXION FUE EXITOSA")

        info = conexion.get_server_info()
        print("LA INFORMACION DEL SERVIDOR ES:",info)
except: 
    print("¡FALLO LA CONEXION")

finally:
    if conexion.is_connected():
        conexion.close()
        print("CONEXION CERRADA EXITOSAMENTE")

       



