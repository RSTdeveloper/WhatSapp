import psycopg2
# Recomendado: https://parzibyte.me/blog/2018/12/20/args-kwargs-python/

def filtrar():
    print("Prueba #1")
    # try:
    #     print("Prueba #2")
    #     conexion = psycopg2.connect(database="rst", user="sophia",password="T34m*-RST", host="192.168.0.122", port= 5432,)
    #     cursor=conexion.cursor()
    #     cursor.execute("SELECT codigo FROM coasmedaslanding.deudores WHERE codigo=1127")

    #     for fila in cursor:
    #         print("FILA= ",fila)
    #     cursor.close()
    #     print("Prueba #3")
    #     return fila
    # except psycopg2.Error as e:
    #     print("Ocurrió un error al conectar a PostgreSQL: ", e)

print("IMPRIMIR = ", filtrar())

