from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

#mysql connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'aerolinea'
mysql = MySQL(app)

def agregar_reservacion(a,b,c,d,e,f,g):
    print(a, g )
    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO reservacion (Nombre, Correo, Telefono, NTarjeta, Fecha, CVV, IDVuelo) VALUES(%s,%s,%s,%s,%s,%s,%s)',
    (a,b,c,d,e,f,g,))
    mysql.connection.commit()
    print("Reservacion agregada con exito")

def buscar_reservacion(data):
    q = "SELECT R.IDReservacion, R.Nombre, R.Correo, V.aerolineaDestino FROM reservacion R JOIN vuelos V ON R.IDVuelo = V.idvuelo WHERE V.destino = '" + data + "'"
    print(q)

