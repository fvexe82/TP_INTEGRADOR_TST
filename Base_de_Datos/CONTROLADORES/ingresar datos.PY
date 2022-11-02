def inserta_Propiedad(self, Id_Propiedad, Id_Tipo, Id_Estado, Id_Operacion_Comercial, Id_Propietario, Nombre, Direccion, Contacto )
    cur = self.cnn.cursor()
    sql = '''INSERT INTO `bd_inmobiliaria`.`propiedad` (`Id_Propiedad`, `Id_Tipo`, `Id_Estado`, `Id_Operacion_Comercial`) VALUES ('1', '5', '1', '1')'''
    cur.execute(sql)
    n=cur.rowcount
    self.cnn.commit()
    cur.close()
    return n