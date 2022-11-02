def Modifica_Propiedad (self, Id_Propiedad ):
    cur = self.cnn.cursor()
    sql = '''UPDATE propiedad SET Id_Tipo = 1 WHERE Id_Propiedad = 11'''.format(Id_Propiedad)
    cur.execute(sql)
    n=cur.rowcount
    self.cnn.commit()
    cur.close()
    return n