import CONTROLADORES.conexion # importamos la variable conexion del modulo conexionbd
import MODELOS.Propiedad #importamos la clase Propiedad
import time
from os import system

def desconectar():
    if conexion.is_connected():
        conexion.close()
        print('LA DESCONEXION SE REALIZÓ CON ÉXITO')

finalizar = False

menu = ("""\
*=====================================================================*
*                         BIENES RAICES FUTURE                        *
*                   SISTEMA DE GESTION DE PROPIEDADES                 *      
*=====================================================================*
|DIGITE SU OPCIÓN:                                                    |
|                                                                     |
| 1. INGRESAR UNA PROPIEDAD                                           |
| 2. MODIFICAR LOS DATOS DE UNA PROPIEDAD                             |
| 3. ELIMINAR UNA PROPIEDAD                                           |
| 4. LISTADO TOTAL DE PROPIEDADES                                     |
| 5. PROPIEDADES DISPONIBLES PARA LA VENTA                            |
| 6. PROPIEDADES DISPONIBLES PARA ALQUILER                            |
| 7. PROPIEDADES VENDIDAS                                             |
| 8. PROPIEDADES ALQUILADAS                                           |
| 9. SALIR                                                            |
*=====================================================================*\
 """)

while not finalizar:
    print(menu)
    try:
        opcion = int(input("INGRESE SU OPCIÓN: "))
        print()
               
        if opcion == 1:
            print('REALIZANDO INGRESO')
        elif opcion == 2:
            print('MODIFICANDO PROPIEDAD')
        elif opcion == 3:
            print('ELIMINANDO PROPIEDAD')
        elif opcion == 4:
            print('LISTANDO LA TOTALIDAD DE PROPIEDADES')
        elif opcion == 5:
            print('PROPIEDADES EN VENTA')
        elif opcion == 6:
            print('PROPIEDADES EN ALQUILER')
        elif opcion == 7:
            print('PROPIEDADES VENDIDAS')
        elif opcion == 8:
            print('PROPIEDADES ALQUILADAS')
        elif opcion == 9:
            print('GRACIAS POR SU CONSULTA')
            desconectar()
            finalizar = True
            time.sleep(1)
            system(cls)
    except:
        print()
        print('OPCIÓN INCORRECTA')
        print()
        continua = input('PRESIONE CUALQUIER TECLA')
        system(cls)

    
