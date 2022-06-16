class Productos():
    __codigo = 0
    __nombre = ""
    __categoria = 0
    __precio = 0

    def __init__(self):
        pass

    def setCodigo(self, cod):
        self.__codigo = cod

    def setNombre(self, nom):
        self.__nombre = nom

    def setCategoria(self, cat):
        self.__categoria = cat

    def setPrecio(self, pre):
        self.__precio = pre

    def getCodigo(self):
        return self.__codigo

    def getNombre(self):
        return self.__nombre

    def getCategoria(self):
        return self.__categoria

    def getPrecio(self):
        return self.__precio