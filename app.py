from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user
from vuelo import cargar_vuelos, agregar_vuelo, modificar_vuelo, eliminar_vuelo
from reservacion import agregar_reservacion, buscar_reservacion, abordar
from models.ModelUser import ModelUser
from models.entities.User import User

app = Flask(__name__)

#mysql connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'aerolinea'
mysql = MySQL(app)
login_manager_app = LoginManager(app)

#settings setting
app.secret_key = 'clavebelica1'


@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(mysql,id)


#inicio del portal
@app.route('/')
def index():
    #cur = mysql.connection.cursor()
    #cur.execute('SELECT idvuelo,destino,fecha,aerolineaDestino FROM vuelos')
    #data = cur.fetchall()
    #print(data)
    data = cargar_vuelos()
    return render_template('vuelos.html', vuelos = data)

#login para admin
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        print(request.form['user'])
        print(request.form['pass'])
        user = User(0,request.form['user'], request.form['pass'])
        logged_user = ModelUser.login(mysql,user)
        if logged_user!= None:
            print("usuario logueado difernte a no")
            if logged_user.password:
                login_user(logged_user)
                print("usuario logeado...")
                #print(login_user)
                #typeUser = ModelUser.get_type_by_user(mysql,request.form['user'])
                #print(typeUser)
                #uid = ModelUser.get_id_by_user(mysql,request.form['user'])

                #session['tipoUser'] = typeUser
                #user_type = ModelUser.get_by_id(mysql,user)
                #print(user_type)
                return redirect(url_for('admin'))
            else:

                flash("invalid password")
        else:
            flash("User not found ...")
            return redirect(url_for('login'))

#menu para admin 
@app.route('/admin', methods = ['GET'])
def admin():
    if request.method == 'GET':
        return render_template('administracion.html')

#logout de admin
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

#pagina para agregar vuelos
@app.route('/agregar_vuelos', methods = ['GET', 'POST'])
def aggVuelo():
    if request.method == 'GET':
        return render_template('agregar_vuelo.html')
    if request.method == 'POST':
        #a = request.form['idvuelo']
        destino = request.form['destino']
        fecha = request.form['fecha']
        hora = request.form['hora']
        aerolineadestino = request.form['aerolineadestino']
        #print(b)
        #cursor = mysql.connection.cursor()
        #b.capitalize()
        #cursor.execute('INSERT INTO vuelos (destino, fecha, hora, aerolineaDestino) VALUES(%s,%s,%s,%s)',
        #(b,c,d,e,))
        #mysql.connection.commit()
        agregar_vuelo(destino,fecha,hora,aerolineadestino)
        flash('Vuelo añadido con exito')
        return render_template('agregar_vuelo.html')


@app.route('/listar_vuelos', methods=['GET'])
def listar_vuelos():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute('SELECT idvuelo, destino, fecha, hora, aerolineadestino FROM vuelos')
        data = cur.fetchall()
        return render_template('listar_vuelos_mod.html', vuelos = data)

@app.route('/mod_vuelo/<id>')
def modifica_vuelo(id):
    if request.method == 'GET':
        #data = vuelo.sel_vuelo(idvuelo)
        cur = mysql.connection.cursor()
        cur.execute('SELECT idvuelo,destino,fecha,hora,aerolineaDestino FROM vuelos WHERE idvuelo = ' + id)
        data = cur.fetchall()
        #data = vuelo.sel_vuelo(cur, idvuelo)
        print(data)
        if data == 0:
            return render_template('no_existe.html')
        else:
            return render_template('modificar_vuelo.html', vuelos = data)

@app.route('/modificar_vuelo', methods=['POST', 'GET'])	
def modificar_vuelo_post():
    if request.method == 'POST':
        idvuelo = request.form['idvuelo']
        destino = request.form['destino']
        fecha = request.form['fecha']
        hora = request.form['hora']
        aerolineaDestino = request.form['aerolineadestino']
        print(idvuelo)
        #cursor = mysql.connection.cursor()
        #cursor.execute('INSERT INTO vuelos (idVuelo, destino, fecha, hora, aerolineaDestino) VALUES(%s,%s,%s,%s,%s)',
        #(a,b,c,d,e,))
        #mysql.connection.commit()
        #flash('Vuelo añadido con exito')
        modificar_vuelo(idvuelo,destino,fecha,hora,aerolineaDestino)
        return redirect(url_for('admin'))

@app.route('/eliminar_vuelo/<id>', methods=['GET'])
def elimi_vuelo(id):
    if request.method == 'GET':
        #a = request.form['idvuelo']
        a = id
        eliminar_vuelo(a)
        return redirect(url_for('admin'))


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
            #return render_template('vuelos.html', vuelos = data)
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
        cur.execute("SELECT R.idreservacion, R.nombre, R.correo, V.aerolineaDestino, R.abordado FROM reservacion R JOIN vuelos V ON R.idvuelo = V.idvuelo WHERE V.destino = '" + a + "'")
        #cur.execute(query)
        data = cur.fetchall()
        #buscar_reservacion(data)
        print(data)
        if data == None:
            return render_template
        return render_template('buscar_reservacionAlt.html', reservacion=data)

@app.route('/actualizar_abordar', methods=['POST'])
def abordado():
    if request.method == 'POST':
        a = request.form['idreservacion']
        abordar(a)
        return redirect(url_for('admin'))

@app.route('/mod_abordar/<id>', methods=['GET'])
def abordsasdasd(id):
    if request.method == 'GET':
        a = id
        abordar(a)
        return redirect(url_for('admin'))
if (__name__) == '__main__':
    app.run(port=3000, debug = True)