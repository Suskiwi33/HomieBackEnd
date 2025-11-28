import db_conexion

user = "root"
password = "system"


conexion = db_conexion.coneccion_bd(user, password)
if conexion:
    print("NIgga")
    conexion.close()
