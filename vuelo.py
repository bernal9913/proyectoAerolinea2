from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

#mysql connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'aerolinea'
mysql = MySQL(app)

#settings setting
app.secret_key = 'clavebelica1'
def cargar_vuelos():
    cur = mysql.connection.cursor()
    cur.execute('SELECT idvuelo,destino,fecha,aerolineaDestino FROM vuelos')
    data = cur.fetchall()
    print(data)
    return data 

def agregar_vuelo(b,c,d,e):
    print(b)
    cursor = mysql.connection.cursor()
    b.capitalize()
    cursor.execute('INSERT INTO vuelos (destino, fecha, hora, aerolineaDestino) VALUES(%s,%s,%s,%s)',
    (b,c,d,e,))
    mysql.connection.commit()

def sel_vuelo(cur, idvuelo):
    #cur = mysql.connection.cursor()
    cur.execute('SELECT idvuelo,destino,fecha,hora,aerolineaDestino FROM vuelos WHERE idvuelo = ' + idvuelo)
    data = cur.fetchall()
    print(data)
    print(cur)
    return data

if __name__ == '__main__':
    sel_vuelo("2")