from os import rename


class Clientes():
    __rut = ""
    __nombre = ""
    __direccion = ""
    __tipo = 0

    def __init__(self):
        pass

    def setRut(self, rut):
        self.__rut = rut

    def setNombre(self, nom):
        self.__nombre = nom

    def setDireccion(self, dir):
        self.__direccion = dir

    def setTipo(self, tip):
        self.__tipo = tip

    def getRut(self):
        return self.__rut

    def getNombre(self):
        return self.__nombre

    def getDireccion(self):
        return self.__direccion

    def getTipo(self):
        return self.__tipo