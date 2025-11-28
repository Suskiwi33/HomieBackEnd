class Usuario:
    def __init__(self, nombre_usuario, contraseña):
        self.id_usuario = None
        self.nombre = nombre_usuario
        self.contraseña = contraseña
    
    def getIdUsuario(self):
        return self.id_usuario
    
    def getNombre(self):
        return self.nombre
    
    def getContraseña(self):
        return self.contraseña
    
    def setNombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre  

    def setContraseña(self, nueva_contraseña):
        self.contraseña = nueva_contraseña