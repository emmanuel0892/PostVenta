import pymysql
from os import system

class DAO():

    def __init__(self):
        pass

    # CONEXIÓN DE LA BASE DE DATOS
    def __conectar(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='VENTAS_BAZAR'
        )

        self.cursor = self.connection.cursor()

    # DESCONEXIÓN DE LA BASE DE DATOS
    def __desconectar(self):
        self.cursor = self.cursor.close()

    # FUNCIÓN PARA AGREGAR USUARIOS - JEFE VENTAS
    def agregarUsuarios(self, u):
        try:
            self.__conectar()
            sql = "INSERT INTO USUARIOS (ID_RUT_US, NOM_US, TIPO_US, USER_US, PASS_US) VALUES (%s,%s,%s,%s,%s);"
            val = (u.getRut(),u.getNombre(),u.getTipo(),u.getUsuario(),u.getContraseña())
            self.cursor.execute(sql,val)
            self.connection.commit()
            self.__desconectar()
            system('cls')
            print("Usuario registrado de manera exitosa!!!")
            system('pause'),
            system('cls')
        except Exception:
            system('cls')
            print("Error al agregar el usuarios!!!")
            system('pause'),
            system('cls')

    # OBTIENE DATOS DE LA TABLA USUARIOS - SISTEMA
    def obtenerUsuarios(self):
        try:
            self.__conectar()
            sql = "SELECT * FROM USUARIOS;"
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
            self.__desconectar()
            return rs
        except Exception:
            system('cls')
            print("A ocurrido un error al realizar la consulta!!!")
            system('pause'),
            system('cls')
            return

    # OBTIENE DATOS DE LA TABLA TIPO USUARIO - SISTEMA
    def selectTipoUs(self, usuario):
        try:
            self.__conectar()
            sql = "SELECT TIPO_USUARIO.NOM_TIP_US FROM USUARIOS INNER JOIN TIPO_USUARIO ON USUARIOS.TIPO_US = TIPO_USUARIO.ID_TIPO_US WHERE USUARIOS.USER_US = '"+usuario+"';"
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
            self.__desconectar()
            tipoUs = (rs[0][0])
            return tipoUs
        except:
            print("")

    # COMPROBACIÓN DE EXISTENCIA DE RUT - SISTEMA
    def comprobarRut(self, rut):
        rs = self.obtenerUsuarios()
        validar = False

        for x in rs:
            if x[0] == rut:
                validar = True

        return validar

    # VALIDAR CREDENCIALES DE USUARIO - SISTEMA
    def validarUsuario(self, user, password):
        validacion = False
        datosU = self.obtenerUsuarios()
        for x in datosU:
            if (x[3] == user and x[4] == password):
                validacion = True
        return validacion

    # INSERTA DATOS AUTOMATICAMENTE A HISTORIAL DE LOGIN - SISTEMA
    def insertHistorialLogin(self, user, rut, tipoU, fecha, hora):
        try:
            self.__conectar()
            sql = "INSERT INTO HISTORIAL_LOGIN (NOM_US_LOG,RUT_US_LOG,TIPO_US_LOG,FEC_LOG,HOR_LOG) VALUES (%s,%s,%s,%s,%s);"
            var = (user,rut,tipoU,fecha,hora)
            self.cursor.execute(sql,var)
            self.connection.commit()
            self.__desconectar()
            rs = self.selectHistoriaL(rut,fecha,hora)
            self.insertNubHistorial(rs)
        except:
            system('cls')
            print("Error al realizar la inserción de datos!!!")
            system('pause')

    # OBTIENE LA INFORMACIÓN DEL HISTORIAL DE LOGIN - SISTEMA
    def selectHistoriaL(self,rut,fecha,hora):
        try:
            self.__conectar()
            sql = "SELECT ID_HIS_LOG,RUT_US_LOG,FEC_LOG,HOR_LOG FROM HISTORIAL_LOGIN WHERE (RUT_US_LOG = %s) AND (FEC_LOG = %s) AND (HOR_LOG = %s);"
            self.cursor.execute(sql,(rut,fecha,hora))
            rs = self.cursor.fetchall()
            self.__desconectar()
            return rs
        except Exception:
            system('cls')
            print("A ocurrido un error al realizar la consulta!!!")
            system('pause'),
            system('cls')
            return

    # INSERTAR DATOS DE LOGEO - SISTEMA
    def insertNubHistorial(self,rs):
        try:
            for x in rs:
                idUs = x[0]
                r = x[1]
            self.__conectar()
            sql = "INSERT INTO NUB_HISTORIAL_LOGIN_USUARIOS (HIS_LOG,RUT_US) VALUES (%s,%s);"
            var = (idUs,r)
            self.cursor.execute(sql,var)
            self.connection.commit()
        except:
            system('cls')
            print("Error al realizar la inserción de datos!!!")
            system('pause')

    # OBTENER PRODUCTOS - VENDEDOR
    def obtenerProductos(self):
        try:
            self.__conectar()
            sql = "SELECT PRODUCTOS.COD_PRO, PRODUCTOS.NOM_PRO, CATEGORIAS.NOM_CAT, PRODUCTOS.PRE_PRO FROM PRODUCTOS INNER JOIN CATEGORIAS ON PRODUCTOS.CAT_PRO = CATEGORIAS.ID_CAT;"
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
            self.__desconectar()
            return rs
        except Exception:
            system('cls')
            print("A ocurrido un error al realizar la consulta!!!")
            system('pause'),
            system('cls')
            return

    # # CUNSULTAR EL ESTADO DEL DÍA PARA APERTURA DE DÍA
    def estadoDia1(self, fecha):
        try:
            val = 0
            self.__conectar()
            sql = "SELECT EST_DIA.NOM_EST, APERTURA_CIERRE.FECHA, APERTURA_CIERRE.HORA FROM APERTURA_CIERRE INNER JOIN EST_DIA ON APERTURA_CIERRE.ESTADO = EST_DIA.ID_EST_DIA;"
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
            self.__desconectar()
            for x in rs:
                if x[0] == "ABIERTO" and x[1] == fecha:
                    val = 1
                elif x[0] == "CERRADO" and x[1] < fecha:
                    val = 0
                elif x[0] == "CERRADO" and x[1] == fecha:
                    val = 2
                    for i in rs:
                        if i[0] == "CERRADO" and i[1] > fecha:
                            val = 3
                        elif i[0] == "ABIERTO" and i[1] > fecha:
                            val = 4
            return val
        except:
            print("Error al realizar la consulta!!!")
    
    # CUNSULTAR EL ESTADO DEL DÍA PARA CIERRE DE DÍA
    def estadoDia2(self, fecha):
        try:
            val = 0
            self.__conectar()
            sql = "SELECT EST_DIA.NOM_EST, APERTURA_CIERRE.FECHA, APERTURA_CIERRE.HORA FROM APERTURA_CIERRE INNER JOIN EST_DIA ON APERTURA_CIERRE.ESTADO = EST_DIA.ID_EST_DIA;"
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
            self.__desconectar()
            if len(rs) == 0:
                val = 3
            else:
                for x in rs:
                    if x[0] == "ABIERTO" and x[1] == fecha:
                        val = 1
                    elif x[0] == "CERRADO" and x[1] == fecha:
                        system('cls')
                        print("El día con fecha ",fecha," se encuentra cerrado!!")
                        system('pause')
                        val = 0
                        for x in rs:
                            if x[0] == "ABIERTO" and x[1] > fecha:
                                val = 2
                    elif x[0] == "CERRADO" and x[1] == fecha:
                        val = 0
            return val
        except:
            print("Error al realizar la consulta!!!")

    # APERTURA DE DÍA - JEFE DE VENTAS
    def aperturaDia(self, estado, fecha, hora):
        try:
            self.__conectar()
            sql = "INSERT INTO APERTURA_CIERRE (ESTADO,FECHA,HORA) VALUES (%s,%s,%s);"
            var = (estado,fecha,hora)
            self.cursor.execute(sql,var)
            self.connection.commit()
            system('cls')
            print("Apertura del día ",fecha," realizado de manera exitosa a las ",hora,"Hrs!!!")
            system('pause')
        except:
            system('cls')
            print("Error al realizar la inserción de datos!!!")
            system('pause')

    # CIERRE DE DÍA - JEFE DE VENTAS
    def cierreDia(self,estado,fecha,hora):
        try:
            self.__conectar()
            sql = "UPDATE APERTURA_CIERRE SET ESTADO = %s, HORA = %s WHERE FECHA = %s;"
            self.cursor.execute(sql,(estado,hora,fecha))
            self.connection.commit()
            system('cls')
            print("Cierre de día realizado de manera exitosa!!!")
            system('pause')
        except:
            system('cls')
            print("Error al realizar la actualización del día!!!")
            system('pause')