from .entities.User import User


class ModelUser():

    @classmethod
    def login(self, mysql, user):
        try:
            cursor = mysql.connection.cursor()
            sql = """SELECT idUser, user, password, nombre FROM adminuser WHERE user = '{}'""".format(user.user)
            cursor.execute(sql)
            row = cursor.fetchone()
            print("ModelUser login: ")
            print(row)
            if row != None:
                user = User(row[0],row[1], row[2],row[3])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT idUser, user, nombre FROM adminuser WHERE idUser = {}".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            print("ModelUser get_by_id")
            print(row)
            if row != None:
                
                logged_user = User(row[0], row[1], None, row[2])
                return logged_user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_type_by_user(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = 'SELECT tipoUser FROM usuarios WHERE user = "' + user + '"'
            cursor.execute(sql)
            row = cursor.fetchone()
            print("Model User get_type_by_user: ")
            print(row)
            if row != None:
                typeUser = row[0]
                return typeUser
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_id_by_user(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = 'SELECT idusuario FROM usuarios WHERE user = "' + user + '"'
            cursor.execute(sql)
            row = cursor.fetchone()
            print("Model User get_id_by_user: ")
            print(row)
            if row != None:
                idUser = row[0]
                return idUser
            else:
                return None
        except Exception as ex:
            raise Exception(ex)