import psycopg2

conec = None
cur = None

def conexion():
    try:
        global conec
        global cur
        conec = psycopg2.connect(host="localhost", database="consul_db", user="postgres", password="pass123")
        print("Conexión con base de datos establecida")
        cur = conec.cursor()
    except:
        print("Error de conexión con base de datos")    

def consultar(sqlquery):
    cur.execute(sqlquery)
    return cur.fetchone()

def cerrar():
    try:
        cur.close()
        conec.close()
        print("Conexión con  base de datos cerrada")
    except:
        print("Error al cerrar conexión")    

conexion()
x = consultar("select * from diagnosticos")
cerrar()
print(x)