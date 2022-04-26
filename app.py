from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from vuelo import cargar_vuelos, agregar_vuelo
from reservacion import agregar_reservacion, buscar_reservacion


app = Flask(__name__)

#mysql connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'aerolinea'
mysql = MySQL(app)

#settings setting
app.secret_key = 'clavebelica1'


#inicio del portal
@app.route('/')
def index():
    #cur = mysql.connection.cursor()
    #cur.execute('SELECT idvuelo,destino,fecha,aerolineaDestino FROM vuelos')
    #data = cur.fetchall()
    #print(data)
    data = cargar_vuelos()
    return render_template('index.html', vuelos = data)

@app.route('/admin', methods = ['GET'])
def admin():
    if request.method == 'GET':
        return render_template('administracion.html')
#pagina para agregar vuelos
@app.route('/agregar_vuelos', methods = ['GET', 'POST'])
def aggVuelo():
    if request.method == 'GET':
        return render_template('agregar_vuelo.html')
    if request.method == 'POST':
        #a = request.form['idvuelo']
        b = request.form['destino']
        c = request.form['fecha']
        d = request.form['hora']
        e = request.form['aerolineadestino']
        #print(b)
        #cursor = mysql.connection.cursor()
        #b.capitalize()
        #cursor.execute('INSERT INTO vuelos (destino, fecha, hora, aerolineaDestino) VALUES(%s,%s,%s,%s)',
        #(b,c,d,e,))
        #mysql.connection.commit()
        agregar_vuelo(b,c,d,e)
        flash('Vuelo añadido con exito')
        return render_template('agregar_vuelo.html')


#no sirve de nada xd
@app.route('/administrar_vuelos', methods=['POST', 'GET'])	
def administrar_vuelos():
    if request.method == 'POST':
        a = request.form['idvuelo']
        b = request.form['destino']
        c = request.form['fecha']
        d = request.form['hora']
        e = request.form['aerolineadestino']
        print(a)
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO vuelos (idVuelo, destino, fecha, hora, aerolineaDestino) VALUES(%s,%s,%s,%s,%s)',
        (a,b,c,d,e,))
        mysql.connection.commit()
        flash('Vuelo añadido con exito')
        return redirect(url_for('/agregar_vuelos'))

#pagina redireccionada con el vuelo en cuestion
@app.route('/vuelo/<string:idvuelo>')
def vuelo(idvuelo):
    if request.method == 'GET':
        #data = vuelo.sel_vuelo(idvuelo)
        cur = mysql.connection.cursor()
        cur.execute('SELECT idvuelo,destino,fecha,hora,aerolineaDestino FROM vuelos WHERE idvuelo = ' + idvuelo)
        data = cur.fetchall()
        #data = vuelo.sel_vuelo(cur, idvuelo)
        print(data)
        if data == 0:
            return render_template('no_existe.html')
        else:
            return render_template('vuelo.html', vuelos = data)
            #return render_template('index.html', vuelos = data)
        #return render_template('vuelo.html', vuelos = data)
    
#pagina para relizar la reservacion
@app.route('/reservacion/<string:idvuelo>', methods = ['GET', 'POST'])
def resv(idvuelo):
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute('SELECT idvuelo, destino FROM vuelos WHERE idvuelo = ' + idvuelo)
        data = cur.fetchall()
        print (data)
        return render_template('reservacion.html', reservacion = data)
    if request.method == 'POST':
        a = request.form['nombre']
        b = request.form['correo']
        c = request.form['telefono']
        d = request.form['tarjeta']
        e = request.form['fecha']
        f = request.form['cvv']
        g = request.form['idvuelo']
        print(a, g )
        return render_template('confirmacion.html')

#guardar la reservacion en post
@app.route('/guardar_reservacion', methods=['POST'])
def res():
    if request.method == 'POST':
        a = request.form['nombre']
        b = request.form['correo']
        c = request.form['telefono']
        d = request.form['tarjeta']
        e = request.form['fecha']
        f = request.form['cvv']
        g = request.form['idvuelo']
        print(a, g )
        #cursor = mysql.connection.cursor()
        #cursor.execute('INSERT INTO reservacion (Nombre, Correo, Telefono, NTarjeta, Fecha, CVV, IDVuelo) VALUES(%s,%s,%s,%s,%s,%s,%s)',
        #(a,b,c,d,e,f,g,))
        #mysql.connection.commit()
        agregar_reservacion(a,b,c,d,e,f,g)
        return render_template('confirmacion.html')

#pagina para confirmar la confirmacion??
@app.route('/confirmacion', methods=['GET'])
def conf():
    if request.method == 'GET':
        render_template('confirmacion.html')

#pagina para el buscar reservacion desde el menu de administración
@app.route('/buscar_reservacion', methods=['GET', 'POST'])
def buscar_reservacion():
    if request.method == 'GET':
        print("sincho")
        return render_template('buscar_reservacion.html')
    

@app.route('/reservaciones', methods=['POST'])
def buscar_reservacions():
    if request.method == 'POST':
        print("serse")
        a = request.form.get('destino')
        cur = mysql.connection.cursor()
        #query = buscar_reservacion(a)
        cur.execute("SELECT R.IDReservacion, R.Nombre, R.Correo, V.aerolineaDestino, R.abordado FROM reservacion R JOIN vuelos V ON R.IDVuelo = V.idvuelo WHERE V.destino = '" + a + "'")
        #cur.execute(query)
        data = cur.fetchall()
        #buscar_reservacion(data)
        print(data)
        if data == None:
            return render_template
        return render_template('buscar_reservacionAlt.html', reservacion=data)

if (__name__) == '__main__':
    app.run(port=3000, debug = True)