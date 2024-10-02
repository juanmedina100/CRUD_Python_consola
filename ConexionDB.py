import pyodbc

def conectarAcces():
    # Ruta al archivo de base de datos .accdb o .mdb
    database_path = r'C:\Users\JIMD\Documents\Personas\PersonasDB.accdb'

    # Crear la conexión ODBC
    conn = pyodbc.connect(
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        r'DBQ=' + database_path + ';'
    )

    # Crear un cursor para ejecutar consultas
    # cursor = conn.cursor()
    return conn
