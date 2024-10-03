from ConexionDB import conectarAcces

def cargarMenu():
    print("1 - Insertar Persona (CREATE)")
    print("2 - Consultar todas las personas ordenadas por edad (READ)")
    print("3 - Actualizar la información de una persona (UPDATE)")
    print("4 - Eliminar Persona de la tabla (DELETE)")
    print("========   Sección de consultas perzonalizadas   ========")
    print("5 - Buscar personas por nombre")
    print("6 - Buscar personas por apellido")
    print("7 - Buscar personas por edad")
    print("0 - Salir")

def ingresarNuevaPersona():
    try:
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
    except:
        conn.close()
        print("No es posible guarfar la información")

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
        conn.close()
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
        conn.close()
        print("**************************************************************")
        print("Ha ocurrido un error al intentar eliminar el registro")
        print("Verifique que el ID ingresado existe en la base de datos")
        print("Verifique que el ID sea un valor numerico")
        print("**************************************************************")

def cargarPersonasOrdenadasPorEdad():
    try:
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
            print(f"ID : {row.id},  Nombres : {row.nombres},   Apellidos : {row.apellidos},   Edad : {row.edad}")
        # Cerrar la conexión
        conn.close()
    except:
        conn.close()

def cargarPersonaPorNombre():
    try:
        conn = conectarAcces()
        # Crear un cursor para ejecutar consultas
        cursor = conn.cursor()

        # Variable a buscar
        buscar = input("Ingresa el nombre : ")
        buscar = f"%{buscar}%"
        # Consultamos la informacion ingresada
        cursor.execute('SELECT id,nombres,apellidos,edad FROM Personas where nombres LIKE ? order by edad asc',(buscar,))
        rows = cursor.fetchall()

        for row in rows:
            print(f"ID : {row.id}, Nombre : {row.nombres}, Apellido : {row.apellidos}, Edad : {row.edad}")
        # Cerrar la conexión
        conn.close()
    except:
        print("================================================================")
        print("La respuesta a tu consulta es : ")
        print("================================================================")

def cargarPersonaPorApellido():
    try:
        conn = conectarAcces()
        # Crear un cursor para ejecutar consultas
        cursor = conn.cursor()

        # Variable a buscar
        buscar = input("Ingresa el apellido : ")
        buscar = f"%{buscar}%"
        # Consultamos la informacion ingresada
        cursor.execute('SELECT id,nombres,apellidos,edad FROM Personas where apellidos LIKE ? order by edad asc',(buscar,))
        rows = cursor.fetchall()

        for row in rows:
            print(f"ID : {row.id}, Nombre : {row.nombres}, Apellido : {row.apellidos}, Edad : {row.edad}")
        # Cerrar la conexión
        conn.close()
    except:
        print("================================================================")
        print("La respuesta a tu consulta es : ")
        print("================================================================")

def cargarPersonaPorEdad():
    try:
        conn = conectarAcces()
        # Crear un cursor para ejecutar consultas
        cursor = conn.cursor()

        # Variable a buscar
        buscar = int(input("Ingresa la edad : "))
        # buscar = f"%{buscar}%"
        # Consultamos la informacion ingresada
        cursor.execute('SELECT id,nombres,apellidos,edad FROM Personas where edad = ? order by edad asc',(buscar,))
        rows = cursor.fetchall()

        for row in rows:
            print(f"ID : {row.id}, Nombre : {row.nombres}, Apellido : {row.apellidos}, Edad : {row.edad}")
        # Cerrar la conexión
        conn.close()
    except:
        print("================================================================")
        print("Error al hacer la petición ")
        print("================================================================")

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
        case 5:
            cargarPersonaPorNombre()
        case 6:
            cargarPersonaPorApellido()
        case 7:
            cargarPersonaPorEdad()
        case 0:
            print("El programa ha finalizado")
            break
