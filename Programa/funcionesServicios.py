# coding=utf-8
import conexion, sqlite3, variables


def insertarServicios(fila):
    """
    Inserta un servicio en una reserva
    :param fila:
        Contiene los datos del servicio
    :return:
        No retorna
    """
    try:

        conexion.cur.execute('insert into servicios (Servicio, Precio, Reserva) values(?,?,?)',fila)
        conexion.conex.commit()
    except Exception as e:
        print("Insertar Servicio Funcion",e)


def borrarServicios(codigo, reserva):
    """
    Borra un servicio
    :param codigo:
        Contiene el codigo del servicio a borrar
    :param reserva:
        Contiene el codigo de la reserva a borrar
    :return:
        No retorna
    """
    try:
        conexion.cur.execute('delete from Servicios where Codigo = ? and Reserva = ?', (codigo, reserva,))
        conexion.conex.commit()
        listadoservicios(variables.listservicios, reserva)

    except Exception as e:
        print("Error modulo eliminar servicios ", e)

# ----------------------------------------------------------------------

def listar(reserva):

    """
    Carga la variable listadoReservas con todos los servicios que pertenezcan a la reserva
    :param reserva:
        Codigo de la reserva asociada al servicio
    :return:
        Retorna una variable con los servicios que tiene dicha reserva
    """
    try:
        conexion.cur.execute('Select * from Servicios where Reserva = ? ',reserva)
        listadoReservas = conexion.cur.fetchall()
        conexion.conex.commit()
        return listadoReservas

    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

# --------------------------------------------------------------------

def listadoservicios(listservicios, reserva):
    """
    Carga el listView de servicios
    :param listservicios:
        Contiene los servicios ya cargados
    :param reserva:
        Contiene el codigo de la reserva
    :return:
        No retorna
    """
    try:
        variables.listado = listar(reserva)
        listservicios.clear()
        for registro in variables.listado:
            listservicios.append(registro[0:3])

    except Exception as e:
        print("Error modulo listado Servicios ",e)

# --------------------------------------------------------------------

def buscarservicios(reserva):
    """
    Busca los servicios de la reserva especificada
    :param reserva:
        Contiene el codigo de la reserva
    :return:
        Retorna los servicios
    """
    try:

        conexion.cur.execute('Select Servicio from Servicios where Reserva = ?', reserva)
        servicios = conexion.cur.fetchall()
        conexion.conex.commit()
        return servicios

    except Exception as e:
        print("Error módulo buscar servicios", e)

# --------------------------------------------------------------------

def buscarservicioprecio(reserva):
    """
    Busca el precio y el servicio de la reserva especificada
    :param reserva:
        Contiene el código de la reserva
    :return:
        Retorna los servicios
    """
    try:

        conexion.cur.execute('Select Servicio, Precio from Servicios where Reserva = ?', reserva)
        servicios = conexion.cur.fetchall()
        conexion.conex.commit()
        return servicios

    except Exception as e:
        print("Error módulo buscar servicios precio", e)

# --------------------------------------------------------------------

def imprimirservicioprecio(reserva):
    """
    Imprime los servicios
    :param reserva:
        Contiene el código de la reserva
    :return:
        No retorna
    """
    try:

        listado = buscarservicioprecio(reserva)
        i = 0

        for i in range (len(variables.conceptosservicios)):
            variables.conceptosservicios[i].set_text('')
            variables.preciosconcepto[i].set_text('')

        i = 0
        for registro in listado:
            variables.conceptosservicios[i].set_text(str(registro[0]))
            variables.preciosconcepto[i].set_text(str(registro[1]))
            i = i + 1
            print("Servicio: "+str(registro[0])+" Precio: "+str(registro[1]))

    except Exception as e:
        print('Error modulo imprimir servicios', e)


# --------------------------------------------------------------------

def comprobarexistencia(reserva, servicio):
    """
    Comprueba que el servicio no este asignado a la reserva
    :param reserva:
        Contiene el código de la reserva
    :param servicio:
        Contiene el codigo del servicio
    :return:
        Retorna el servicio si lo encuentra
        Retorna null si no lo encuentra
    """
    servicios = buscarservicios(reserva)

    b = 0

    for registro in servicios:
        if registro[0] == servicio:
            b = 1

    if b == 1:
        return servicio
    else:
        return ''
