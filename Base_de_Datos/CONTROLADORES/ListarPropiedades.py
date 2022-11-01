
from Conexion import conexion

cursor=conexion.cursor()
cursor.execute("SELECT * from Propiedad")
for x in cursor:
    print(x)
conexion.close()
print("CONEXION CERRADA EXITOSAMENTE")
