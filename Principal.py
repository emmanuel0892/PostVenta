from os import system
from Funciones import Funciones
from Funciones import colores
from DAO import DAO
from datetime import datetime

class Principal():

    f = Funciones()
    d = DAO()
    c = colores()

    def __init__(self):
        pass

    def ejecutarSistemaVentas(self,user):
        self.f.Menu(user)

    # LOGIN DE USUARIOS - SISTEMA
    def controlUsuarios(self):
        system('cls')
        print(colores.verde+" _________________________________")
        print("|               "+colores.amarillo+"Login"+colores.verde+"             |")
        print(" ---------------------------------"+colores.reset)
        user = self.f.digitarTexto1(30, "el USUARIO")
        system('cls')
        print(colores.verde+" _________________________________")
        print("|               "+colores.amarillo+"Login"+colores.verde+"             |")
        print(" ---------------------------------"+colores.reset)
        pas  = self.f.digitarTexto2(30,"la CONTRASEÑA")
        validar = self.d.validarUsuario(user,pas)
        if(validar == True):
            #llamar a la funcion para insertar datos en historial de logeo
            rs = self.d.obtenerUsuarios()

            f = datetime.now()
            fe = f.date()
            ho = f.time()
            fecha = fe
            hora = ho
            hora = hora.replace(microsecond=0)
            for x in rs:
                if x[3] == user:
                    rut = x[0]
                    tipo = x[2]
            self.d.insertHistorialLogin(user,rut,tipo,fecha,hora)
            self.ejecutarSistemaVentas(user)
        else:
            try:
                print("El usuario o la contraseña es incorrecto!!!")
                res = self.f.Pregunta1("Decea reintentar")
                assert res == 1 or res == 2
                if(res == 1):
                    system('cls')
                    p.controlUsuarios()
                elif(res == 2):
                    system('cls')
                    print(self.c.amarillo+"Adiós"+self.c.reset)
                    system('pause')
                    system('cls')
                    return
            except AssertionError:
                print("La opción seleccionada es incorrecta, intente nuevamente!!!")

p = Principal()
p.controlUsuarios()