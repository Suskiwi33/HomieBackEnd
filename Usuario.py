class Usuario:
    def __init__(self, nombre_usuario, contraseña, correo):
        self.id_usuario = None
        self.nombre = nombre_usuario
        self.contraseña = contraseña
        self.correo = correo
    
    def getIdUsuario(self):
        return self.id_usuario
    
    def getNombre(self):
        return self.nombre
    
    def getContraseña(self):
        return self.contraseña
    
    def getCorreo(self):
        return self.correo
    
    def setNombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre  

    def setContraseña(self, nueva_contraseña):
        self.contraseña = nueva_contraseña
    
    def setCorreo(self, nuevo_correo):
        self.correo = nuevo_correo