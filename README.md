# CRUD_Python_consola
## CRUD usando base de datos de access

Un pequeño sistema de practica aplicando un CRUD (CREATE,READ,UPDATE,DELETE) 
usando Python con consola.

La base de datos que se esta usando es de Microsoft Access.

Aca la función que se usa para poder acceder a la base de datos:

```python
import pyodbc

def conectarAcces():
    # Ruta al archivo de base de datos .accdb o .mdb
    database_path = r'C:\Users\MyUser\Documents\Personas\PersonasDB.accdb'

    # Crear la conexión ODBC
    conn = pyodbc.connect(
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        r'DBQ=' + database_path + ';'
    )

    # Crear un cursor para ejecutar consultas
    return conn
```
La información de la conexión esta en la base del programa como ConexionDB.py.


![conexionpyaccess.png](imagenes%2Fconexionpyaccess.png)


Importamos la conexión para usarla un cualquier parte de la plicación.

```python
from ConexionDB import conectarAcces
```

El menu para la aplicación CRUD es:
```python
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
```

Función para hacer un CREATE a la tabla de la base de datos:
```python
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
        print("No es posible guardar la información")
```

Función para hacer un READ a la tabla de la base de datos:
```python
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
```
Función para hacer un UPDATE a la tabla de la base de datos:
```python
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
```
Función para hacer un DELETE a la tabla de la base de datos:
```python
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
```
 Es importante antes crer una base de datos en acces con la siguiente información:

 Nombre del archivo de access: *PersonasDB.accdb*

 Nombre de la tabla : *Personas*

 Los campos de la tabl deben tener la siguiente estructura:
 
![estructurapersonas.png](imagenes%2Festructurapersonas.png)
