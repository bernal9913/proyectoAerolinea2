from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

#mysql connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'aerolinea'
mysql = MySQL(app)

def agregar_reservacion(nombre,correo,telefono,nTarjeta,fecha,cvv,idvuelo):
    print(nombre, idvuelo )
    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO reservacion (combre, correo, telefono, nTarjeta, fecha, cvv, idvuelo) VALUES(%s,%s,%s,%s,%s,%s,%s)',
    (nombre, correo, telefono, nTarjeta, fecha, cvv, idvuelo,))
    mysql.connection.commit()
    print("Reservacion agregada con exito")

def buscar_reservacion(data):
    q = "SELECT R.ideservacion, R.nombre, R.correo, V.aerolineaDestino FROM reservacion R JOIN vuelos V ON R.idvuelo = V.idvuelo WHERE V.destino = '" + data + "'"
    print(q)

def abordar(idreservacion):
    print(idreservacion)
    cursor = mysql.connection.cursor()
    cursor.execute('UPDATE reservacion SET abordado = "SI" WHERE idreservacion = ' + idreservacion)
    mysql.connection.commit()
    print("Usuario abordado exitosamente")
