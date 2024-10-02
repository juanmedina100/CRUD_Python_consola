from ConexionDB import conectarAcces

def cargarMenu():
    print("1 - Insertar Persona (CREATE)")
    print("2 - Consultar todas las personas ordenadas por edad (READ)")
    print("3 - Actualizar la información de una persona (UPDATE)")
    print("4 - Eliminar Persona de la tabla (DELETE)")
    print("0 - Salir")

def ingresarNuevaPersona():
    conn = conectarAcces()
    # Crear un cursor para ejecutar consultas
    cursor = conn.cursor()
    insertRegistro = '''
        insert into Personas(nombres,apellidos,edad,direccion) values(?,?,?,?)
    '''
    nombres = input("Escribe el nombre : ")
    apellido = input("Escribe el apellido : ")
    edad = int(input("Escribe la edad : "))
    direccion = input("Escribe la dirección : ")

    valoresInsertar = (nombres, apellido, edad, direccion)
    cursor.execute(insertRegistro, valoresInsertar)
    conn.commit()
    # Cerrar la conexión
    conn.close()

def actualizarPersona():
    try:
        conn = conectarAcces()
        # Crear un cursor para ejecutar consultas
        cursor = conn.cursor()
        idActualizar = int(input("Escribe el ID del registro a Actualizar : "))

        # Debemos comprobar si existe el registro
        buscarRegistro = ''' select * from Personas where id = ? '''
        cursor.execute(buscarRegistro,(idActualizar,))
        registro = cursor.fetchone()
        if registro:
            actualizarRegistro = '''
                update Personas set nombres=?,apellidos=?,edad=?,direccion=? where id = ?
            '''
            nombres = input("Escribe el nombre : ")
            apellido = input("Escribe el apellido : ")
            edad = int(input("Escribe la edad : "))
            direccion = input("Escribe la dirección : ")
            # valoresActualizar = (nombres, apellido, edad, direccion)
            cursor.execute(actualizarRegistro,(nombres,apellido,edad,direccion,idActualizar))
            conn.commit()
            print(f"El registro {idActualizar} fue actualizado")
        else:
            print(f"El registro {idActualizar} no existe.")
    except:
        print("**************************************************************")
        print("Ha ocurrido un error al intentar actualizar el registro")
        print("Verifique que el ID ingresado existe en la base de datos")
        print("Verifique que el ID sea un valor numerico")
        print("**************************************************************")
def eliminarPersona():
    try:
        conn = conectarAcces()
        # Crear un cursor para ejecutar consultas
        cursor = conn.cursor()
        idEliminar = int(input("Escribe el ID del registro a eliminar : "))

        # Debemos comprobar si existe el registro
        buscarRegistro = ''' select * from Personas where id = ? '''
        cursor.execute(buscarRegistro,(idEliminar,))
        registro = cursor.fetchone()
        if registro:
            eliminarRegistro = '''
                delete from Personas where id = ?
            '''
            cursor.execute(eliminarRegistro,(idEliminar,))
            conn.commit()
            print(f"El registro {idEliminar} fue eliminado")
        else:
            print(f"El registro {idEliminar} no existe.")
    except:
        print("**************************************************************")
        print("Ha ocurrido un error al intentar eliminar el registro")
        print("Verifique que el ID ingresado existe en la base de datos")
        print("Verifique que el ID sea un valor numerico")
        print("**************************************************************")

def cargarPersonasOrdenadasPorEdad():
    conn = conectarAcces()
    # Crear un cursor para ejecutar consultas
    cursor = conn.cursor()
    # Consultamos la informacion ingresada
    cursor.execute('SELECT id,nombres,apellidos,edad FROM Personas order by edad asc')
    rows = cursor.fetchall()
    print("================================================================")
    print("La respuesta a tu consulta es : ")
    print("================================================================")
    for row in rows:
        print(row)
    # Cerrar la conexión
    conn.close()

while(True):
    print("================================================================")
    print("Bienvenido al mini sistema para ingresar y consultar personas (CRUD)")
    print("================================================================")
    cargarMenu()
    respuesta = int(input(""))
    match respuesta:
        case 1:
            ingresarNuevaPersona()
        case 2:
            cargarPersonasOrdenadasPorEdad()
        case 3:
            actualizarPersona()
        case 4:
            eliminarPersona()
        case 0:
            print("El programa ha finalizado")
            break
