import mysql.connector

try:
    conexion = mysql.connector.connect(host = 'localhost',
                                    user='root',
                                    password='',
                                    database='usarios_login')


except Exception as err:
    print('ERROR CONECTANDO A LA BASE')
else:
    print('CONEXIÓN EXITOSA')

    cur01 = conexion.cursor()
    insertar = "insert into usarios value(1, 'sebastian', 'saldarriaga', 'sebas@gmail.com', 'sebas123')"
    cur01.execute(insertar)
    conexion.commit()

conexion.close()
