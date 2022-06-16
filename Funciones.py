from os import system
from DAO import DAO
from Usuarios import Usuarios
from itertools import cycle
from beautifultable import BeautifulTable
from datetime import datetime, timedelta

#CLASE PARA COLOREAR LAS SALIDAS DE TEXTOS
class colores():
    #texto negritas con colores
    rojo     = '\x1b[1;31m'
    amarillo = '\x1b[1;33m'
    negro    = '\x1b[1;30m'
    verde    = '\x1b[1;32m'
    azul     = '\x1b[1;34m'
    morado   = '\x1b[1;35m'
    blanco   = '\x1b[1;37m'
    reset    = '\033[0;m'

    #texto de colores y oculto
    rojo1     = '\x1b[6;31m'
    amarillo1 = '\x1b[6;33m'
    negro1    = '\x1b[6;30m'
    verde1    = '\x1b[6;32m'
    azul1     = '\x1b[6;34m'
    morado1   = '\x1b[6;35m'
    blanco1   = '\x1b[6;37m'

    #texto colores debiles
    rojo2     = '\x1b[2;31m'
    amarillo2 = '\x1b[2;33m'
    negro2    = '\x1b[2;30m'
    verde2    = '\x1b[2;32m'
    azul2     = '\x1b[2;34m'
    morado2   = '\x1b[2;35m'
    blanco2   = '\x1b[2;37m'

    #texto subrayado
    rojo3     = '\x1b[4;31m'
    amarillo3 = '\x1b[4;33m'
    negro3    = '\x1b[4;30m'
    verde3    = '\x1b[4;32m'
    azul3     = '\x1b[4;34m'
    morado3   = '\x1b[4;35m'
    blanco3   = '\x1b[4;37m'

class Funciones(): 
    global usu
    usu = ""

    d = DAO() 

    def __init__(self):
        pass

    # VALIDACION DEL INGRESO DE TEXTO1
    def digitarTexto1(self, cantidad, texto):
        try:
            #este contador permite que solo se vizualice el contenido del usuario posterior al logueo
            cont = 0
            cont = cont + cont
            if(cont > 0):
                print("Usuario actual: "+usu+"\n")
            t = input(colores.amarillo+"Ingrese "+texto+" :"+colores.rojo+"\n--> "+colores.reset)
            assert len(t.strip()) >= 1 and len(t.strip()) <= cantidad
            v = t.strip().isnumeric()
            if v == True:
                self.digitarTexto1()
            return t
        except AssertionError:
            system('cls')
            print("Usuario actual: "+usu+"\n")
            print("El texto debe tener un largo minimo de 1 caracter y máximo de "+str(cantidad)+" caracteres!!!")
            system('pause')
            system('cls')
            self.digitarTexto1(cantidad,texto)

        except Exception:
            system('cls')
            print("Usuario actual: "+usu+"\n")
            print("Error, solo se admite texto en este campo!!!")
            system('pause')
            system('cls')
            self.digitarTexto1(cantidad,texto)

    # VALIDACION DEL INGRESO DE TEXTO2
    def digitarTexto2(self, cantidad, texto):
        try:
            cont = 0
            cont = cont + cont
            if(cont > 0):
                print("|"+colores.amarillo+" Usuario actual: "+colores.verde+"",usu,""+colores.blanco+"|"+colores.amarillo+" Tipo de Usuario: "+colores.verde+"",tipo,colores.blanco+"|"+colores.reset)
            t = input(colores.amarillo+"Ingrese "+texto+" :"+colores.rojo+"\n--> "+colores.reset)
            assert len(t.strip()) >= 1 and len(t.strip()) <= cantidad
            return t
        except AssertionError:
            system('cls')
            print("|"+colores.amarillo+" Usuario actual: "+colores.verde+"",usu,""+colores.blanco+"|"+colores.amarillo+" Tipo de Usuario: "+colores.verde+"",tipo,colores.blanco+"|"+colores.reset)
            print("El texto debe tener un largo minimo de 1 caracter y máximo de "+str(cantidad)+" caracteres!!!")
            system('pause')
            system('cls')
            self.digitarTexto2(cantidad,texto)

        except Exception:
            system('cls')
            print("|"+colores.amarillo+" Usuario actual: "+colores.verde+"",usu,""+colores.blanco+"|"+colores.amarillo+" Tipo de Usuario: "+colores.verde+"",tipo,colores.blanco+"|"+colores.reset)
            print("Error, Intentelo nuvamente!!!")
            system('pause')
            system('cls')
            self.digitarTexto2(cantidad,texto)

    # VALIDACION DEL INGRESO DE RUT
    def __digitarRut(self, cantidad, texto):
        try:
            system('cls')
            print("|"+colores.amarillo+" Usuario actual: "+colores.verde+"",usu,""+colores.blanco+"|"+colores.amarillo+" Tipo de Usuario: "+colores.verde+"",tipo,colores.blanco+"|"+colores.reset)
            print("\n")
            t = input(colores.amarillo+"Ingrese "+texto+" :"+colores.verde+"\n--> "+colores.reset)
            assert len(t.strip()) == cantidad
            system('cls')
            return t
        except AssertionError:
            system('cls')
            print("\n")
            print("|"+colores.amarillo+" Usuario actual: "+colores.verde+"",usu,""+colores.blanco+"|"+colores.amarillo+" Tipo de Usuario: "+colores.verde+"",tipo,colores.blanco+"|"+colores.reset)
            print("El rut debe tener un largo de "+str(cantidad)+" caracteres!!!")
            system('pause')
            system('cls')
            self.__digitarRut(cantidad,texto)

        except Exception:
            system('cls')
            print("|"+colores.amarillo+" Usuario actual: "+colores.verde+"",usu,""+colores.blanco+"|"+colores.amarillo+" Tipo de Usuario: "+colores.verde+"",tipo,colores.blanco+"|"+colores.reset)
            print("\n")
            print("Error, el rut debe tener un lagor de "+str(cantidad)+" caracteres, intentelo nuevamente!!!")
            system('pause')
            system('cls')
            self.__digitarRut(cantidad,texto)

    # VALIDACION DEL INGRESO DE NUMEROS
    def __digitarNumero(self, inicio, termino, texto):
        try:
            n = int(input(colores.blanco+"Ingrese "+texto+" :"+colores.amarillo+"\n--> "+colores.reset))
            assert n >= inicio and n <= termino
            return n
        except AssertionError:
            system('cls')
            print("|"+colores.amarillo+" Usuario actual: "+colores.verde+"",usu,""+colores.blanco+"|"+colores.amarillo+" Tipo de Usuario: "+colores.verde+"",tipo,colores.blanco+"|"+colores.reset)
            print("\n")
            print(colores.rojo+"El número ingresado debe ser mayor o igual a "+str(inicio)+" y menor o igual a "+str(termino)+", Error!!!"+colores.reset)
            system('pause')
            system('cls')
            self.__digitarNumero(inicio,termino,texto)
        except ValueError:
            system('cls')
            print("|"+colores.amarillo+" Usuario actual: "+colores.verde+"",usu,""+colores.blanco+"|"+colores.amarillo+" Tipo de Usuario: "+colores.verde+"",tipo,colores.blanco+"|"+colores.reset)
            print("\n")
            print(colores.rojo+"En este campo solo se admiten números"+colores.reset)
            system('pause')
            system('cls')
            val = ""
            return val
            
    # METODO PARA GENERAR PREGUNTAS
    def Pregunta1(self, pregunta):
        try:
            system('cls')
            print(colores.amarillo3+"¿"+pregunta+"?"+colores.reset)
            print("--------------------------")
            print(colores.amarillo+"1-"+colores.blanco+" para SI"+colores.reset)
            print(colores.amarillo+"2-"+colores.blanco+" para NO"+colores.reset+"\n")
            res = int(input(colores.amarillo+"Seleccione una opción:"+colores.amarillo+"\n--> "+colores.reset))
            assert res == 1 or res == 2
            return res
        except AssertionError:
            system('cls')
            print("Usuario actual: "+usu+"\n")
            print(colores.rojo+"Solo puede selecciónar como respuesta 1 o 2, intente nuevamente!!!"+colores.reset)        
            system('pause')
            system('cls')
            self.Pregunta1(pregunta)

    # MENU PRINCIPAL
    def Menu(self,user):
        #se declara variable global para le uso de nombre de usuario actual en las demas clases
        global usu
        global tipo
        tipo = ""
        usu = ""
        usu = user
        op = 0

        tipo = self.d.selectTipoUs(usu)

        system('cls')
        print("|"+colores.amarillo+" Usuario actual: "+colores.verde+"",usu,""+colores.blanco+"|"+colores.amarillo+" Tipo de Usuario: "+colores.verde+"",tipo,""+colores.blanco+"|"+colores.reset)
        print(colores.verde+" _____________________________ ")
        print("|____________"+colores.amarillo+"MENU"+colores.verde+"_____________|")
        print("|                             |")
        if(tipo == "ADMINISTRADOR"):
            print("|"+colores.rojo+" 1- Nueva Venta"+colores.verde+"              |")
            print("|"+colores.blanco+" 2- Apertura de dia"+colores.verde+"          |")
            print("|"+colores.blanco+" 3- Cierre del dia"+colores.verde+"           |")
            print("|"+colores.blanco+" 4- Emisión de informes"+colores.verde+"      |")
            print("|"+colores.blanco+" 5- Gestión inventario"+colores.verde+"       |")
            print("|"+colores.blanco+" 6- Gestión de usuarios"+colores.verde+"      |")
            print("|"+colores.blanco+" 7- Salir"+colores.verde+"                    |")
            print("|_____________________________|\n"+colores.reset)
        else:
            print("|"+colores.blanco+" 1- Nueva Venta"+colores.verde+"              |")
            print("|"+colores.rojo+" 2- Apertura de dia"+colores.verde+"          |")
            print("|"+colores.rojo+" 3- Cierre del dia"+colores.verde+"           |")
            print("|"+colores.rojo+" 4- Emisión de informes"+colores.verde+"      |")
            print("|"+colores.rojo+" 5- Gestión inventario"+colores.verde+"       |")
            print("|"+colores.rojo+" 6- Gestión de usuarios"+colores.verde+"      |")
            print("|"+colores.blanco+" 7- Salir"+colores.verde+"                    |")
            print("|_____________________________|\n"+colores.reset)
        
        op = self.__digitarNumero(1,7,"una de las opciones")

        f = datetime.now()
        fecha = f.date()

        if(op == 1 and tipo == "VENDEDOR"):
            res = self.d.estadoDia1(fecha)
            if res == 1:
                self.nuevaVenta()
            elif res == 2:
                system('cls')
                print("El día esta cerrado, no se admiten más ventas!!!")
                system('pause')
                self.Menu(usu)
            else:
                system('cls')
                print("No se a realizado la apertura del día, comuniquese con Jefe de Ventas!!!")
                system('pause')
                self.Menu(usu)
        elif(op == 2 and tipo == "ADMINISTRADOR"):
            self.aperturaDia()
        elif(op == 3 and tipo == "ADMINISTRADOR"):
            self.cierreDia()
        elif(op == 4 and tipo == "ADMINISTRADOR"):
            #emision de informes (JEFE DE VENTAS)
            pass
        elif(op == 5 and tipo == "ADMINISTRADOR"):
            #gestión inventario (JEFE DE VENTAS)
            pass
        elif(op == 6 and tipo == "ADMINISTRADOR"):
            self.GestionUsuarios()
        elif(op == 7):
            system('cls')
            print(colores.blanco+"Adiós "+colores.amarillo+usu+colores.reset)
            return
        elif(op == ""):
            self.Menu(usu)
        else:
            system('cls')
            print("|"+colores.amarillo+" Usuario actual: "+colores.verde+"",usu,""+colores.blanco+"|"+colores.amarillo+" Tipo de Usuario: "+colores.verde+"",tipo,""+colores.blanco+"|"+colores.reset)
            print("\n")
            print(colores.rojo+"Error, no tiene los privilegios para realizar esta acción!!!"+colores.reset)
            system('pause')
            system('cls')
            self.Menu(usu)

    # MENU GESTION DE USUARIOS - JEFE VENTAS
    def GestionUsuarios(self):
        
        try:
            system('cls')
            print("|"+colores.amarillo+" Usuario actual: "+colores.verde+"",usu,""+colores.blanco+"|"+colores.amarillo+" Tipo de Usuario: "+colores.verde+"",tipo,colores.blanco+"|"+colores.reset)
            print(colores.verde+" ____________________________ ")
            print("|____________"+colores.amarillo+"MENU"+colores.verde+"____________|")
            print("|                            |")
            print("|"+colores.blanco+"1- Agregar Usuario"+colores.verde+"          |")
            print("|"+colores.blanco+"2- Modificar Usuario"+colores.verde+"        |")
            print("|"+colores.blanco+"3- Eliminar Usuario"+colores.verde+"         |")
            print("|"+colores.blanco+"4- Atras"+colores.verde+"                    |")
            print("|____________________________|"+colores.reset)

            op = self.__digitarNumero(1,4,"una de las opciones")

            if(op == 1):
                system('cls')
                self.registarUsuario()
            elif(op == 2):
                pass
            elif(op == 3):
                pass
            elif(op == 4):
                system('cls')
                self.Menu(usu)

        except AssertionError:
            print("")

    # FUNCIÓN PARA VALIDAR QUE EL RUT SEA VÁLIDO
    def validarRut(self,rut):
        rut = rut.upper()
        rut = rut.replace("-","")
        rut = rut.replace(".","")
        aux = rut[:-1]
        dv = rut[-1:]
    
        revertido = map(int, reversed(str(aux)))
        factors = cycle(range(2,8))
        s = sum(d * f for d, f in zip(revertido,factors))
        res = (-s)%11
    
        if str(res) == dv:
            return True
        elif dv=="K" and res==10:
            return True
        else:
            return False

    # NUEVA VENTA - VENDEDOR
    def nuevaVenta(self):
        system('cls')
        r = self.Pregunta1("Decea listar los productos y sus codigos antes de iniciar la venta")
        if r == 1:
            rs = self.d.obtenerProductos()
            tabla = BeautifulTable()
            tabla.column_headers = ["CODIGO","NOMBRE","CATEGORIA","PRECIO_U"]
            for i in rs:
                tabla.rows.append([i[0],i[1],i[2],i[3]])
            system('cls')
            print(tabla)
            system('pause')
            self.Menu(usu)
        else:
            pass

    # RESGISTRAR USUARIOS - JEFE VENTAS
    def registarUsuario(self):
        system('cls')
        validar = True

        while validar == True:
            system('cls')
            val = False
            print("Usuario actual: "+usu+"\n")
            rut = self.__digitarRut(10, "el rut del usuario sin puntos (11111111-1)")
            val = self.validarRut(rut)
            if val == True:
                system('cls')
                validar = self.d.comprobarRut(rut)
                if validar == True:
                    system('cls')
                    print("Usuario actual: "+usu+"\n")
                    self.Pregunta1("El rut ingresado ya existe, deceas volver a intentarlo")
                    if self.Pregunta1() == 1:
                        self.registarUsuario()
                    else:
                        return
            else:
                system('cls')
                print("El rut ingresado no es válido, porfavor ingrese un rut válido!!!")
                system('pause')
                system('cls')
                self.registarUsuario()
        print("Usuario actual: "+usu+"\n")
        nom = self.digitarTexto1(100, "El nombre de la persona")
        system('cls')
        print("Usuario actual: "+usu+"\n")
        print("Seleccióne:")
        print("------------------------------")
        print("\n1- ADMINISTRADOR")
        print("2- VENDEDOR\n")
        print("Usuario actual: "+usu+"\n")
        tip = self.__digitarNumero(1,2, "el tipo de usuario")
        system('cls')
        print("Usuario actual: "+usu+"\n")
        user = self.digitarTexto1(30, "nombre de usuarios para la cuenta")
        system('cls')
        print("Usuario actual: "+usu+"\n")
        con = self.digitarTexto2(30, "la contraseña para la cuenta")

        U = Usuarios()
        U.setRut(rut)
        U.setNombre(nom)
        U.setTipo(tip)
        U.setUsuario(user)
        U.setContraseña(con)

        self.d.agregarUsuarios(U)
        self.Menu(usu)

    # MODIFICAR USUARIOS - JEFE VENTAS
    def modificarUsuario(self):
        pass

    # ELIMINAR USUARIO - JEFE VENTAS
    def eliminarUsuario(slef):
        pass

    # APAERTURA DE DÍA - JEFE VENTAS
    def aperturaDia(self):
        val = datetime.now()
        fecha = val.date()
        hora = val.time()
        hora = hora.replace(microsecond=0)
        r = self.d.estadoDia1(fecha)
        if r == 1:
            system('cls')
            print("La apertura de este dia ",fecha," ya está realizada!!!")
            system('pause')
            self.Menu(usu)
        elif r == 0:
            estado = 1
            self.d.aperturaDia(estado,fecha,hora)
            self.Menu(usu)
        elif r == 2:
            res = self.Pregunta1("Esta seguro de querer abrir un día con fecha de mañana")
            if res == 1:
                estado = 1
                fecha = fecha + timedelta(days=1)
                self.d.aperturaDia(estado,fecha,hora)
                self.Menu(usu)
            if res == 2:
                self.Menu(usu)
        elif r == 3:
            system('cls')
            print("No se puede realizar la apertura de otro día, ya que se encuentra 1 día futuro con fecha ",fecha," cerrado!!!")
            print("\nSE ASEPTA MÁXIMO DE 1 DÍA DE DESFACE!!!")
            system('pause')
            self.Menu(usu)
        elif r == 4:
            system('cls')
            print("No se puede realizar la apertura de otro día, ya que se encuentra 1 día futuro con fecha ",fecha," abierto!!!")
            print("\nSE ASEPTA MÁXIMO DE 1 DÍA DE DESFACE!!!")
            system('pause')
            self.Menu(usu)

    # CIERRE DE DÍA - JEFE VENTAS
    def cierreDia(self):
        val = datetime.now()
        fecha = val.date()
        hora = val.time()
        hora = hora.replace(microsecond=0)
        r = self.d.estadoDia2(fecha)
        if r == 0:
            self.Menu(usu)
        elif r == 1:
            estado = 2
            self.d.cierreDia(estado,fecha,hora)
            self.Menu(usu)
        elif r == 2:
            res2 = self.Pregunta1("Existe la apertura de un día futuro, decea realizar el cierre")
            if res2 == 1:
                estado = 2
                fecha = fecha + timedelta(days=1)
                self.d.cierreDia(estado,fecha,hora)
                self.Menu(usu)
        elif r == 3:
            system('cls')
            print("No existen registros de apertura o cierre!!!")
            system('pause')
            self.Menu(usu)
            

    # MENU EMISIÓN DE INFORMES - JEFE VENTAS
    def menuEmisionInfo(slef):
        pass

    # VENTAS CON BOLETA - VENDEDOR
    def ventasBoleta(self):
        pass

    # VENTAS CON FACTURA - VENDEDOR
    def ventasFactura(self):
        pass

    # MENU GESTION INVENTARIO - JEFE VENTAS
    def menuInventario(self):
        pass

    # AGREGAR PRODUCTOS - JEFE VENTAS
    def agregarPro(self):
        pass

    # MODIFICAR PRODUCTOS - JEFE VENTAS
    def modificarPro(self):
        pass

    # ELIMINAR PRODUTOS - JEFE VENTAS
    def eliminarPro(self):
        pass