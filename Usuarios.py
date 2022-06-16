class Usuarios():
    __rut = ""
    __nombre = ""
    __tipo = 0
    __usuario = ""
    __contraseña = ""
    __sesion = ""

    def __init__(self):
        pass

    def setRut(self, rut):
        self.__rut = rut

    def setNombre(self, nom):
        self.__nombre = nom

    def setTipo(self, tip):
        self.__tipo = tip

    def setUsuario(self, usu):
        self.__usuario = usu

    def setContraseña(self, cont):
        self.__contraseña = cont

    def setSesion(self, ses):
        self.__sesion = ses

    def getRut(self):
        return self.__rut

    def getNombre(self):
        return self.__nombre

    def getTipo(self):
        return self.__tipo

    def getUsuario(self):
        return self.__usuario

    def getContraseña(self):
        return self.__contraseña

    def getSesion(self):
        return self.__sesion