from psycopg2 import connect
# import supabase as supabase
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from config import Config

# from flask_mysqldb import MySQL

app = Flask(__name__)
app.config.from_object(Config)
# Settings session
app.secret_key = app.config['SECRET_KEY'],


# mysql = MySQL(app)

# Supabase Connection con Postgres
def get_db_conn():
    return connect(
        dbname=app.config['DB_NAME'],
        user=app.config['DB_USER'],
        password=app.config['DB_PASSWORD'],
        host=app.config['DB_HOST'],
        port=app.config['DB_PORT'],
    )


# Inicio con video
@app.route('/')
def inicio():
    return render_template('index.html')


# Home de la agenda
@app.route('/home', methods=['GET'])
def home():
    if request.method == 'GET':
        conexion = get_db_conn()
        cursor = conexion.cursor()
        data_json = []
        try:
            cursor.execute("SELECT * FROM users ORDER BY id asc")
            data = cursor.fetchall()
            for registro in data:
                registro_json = {
                    'id': registro[0],
                    'creado': registro[1],
                    'fullName': registro[2],
                    'phone': registro[3],
                    'email': registro[4]
                }
                data_json.append(registro_json)
            flash('Contactos obtenidos con éxito', 'success')
        except Exception as e:
            flash(f'Error al obtener los contactos: {str(e)}', 'error')
        finally:
            cursor.close()
            conexion.close()
            return render_template('home.html', contactos=data_json, disableCancelButton=True)
    return


# Alta de contacto
@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        conexion = get_db_conn()
        cursor = conexion.cursor()
        try:
            cursor.execute('''INSERT INTO users (fullName, phone, email) VALUES (%s, %s, %s)''',
                           (request.form['fullName'], request.form['phone'], request.form['email']))
            conexion.commit()
            flash('Contacto agregado con éxito', 'success')
        except Exception as e:
            flash(f'Error al agregar el contacto: {str(e)}', 'error')
        finally:
            cursor.close()
            conexion.close()
            return redirect(url_for('home'))
    return


# Baja de contacto
@app.route('/delete_contact/<string:id_contact>', methods=['GET'])
def delete_contact(id_contact):
    if request.method == 'GET':
        conexion = get_db_conn()
        cursor = conexion.cursor()
        try:
            cursor.execute('DELETE FROM users WHERE id = {0}'.format(id_contact))
            conexion.commit()
            flash(f'Contacto con la id {id_contact} eliminado con éxito.', 'success')
        except Exception as e:
            flash(f'Error al eliminar el contacto: {str(e)}', 'error')
        finally:
            cursor.close()
            conexion.close()
            return redirect(url_for('home'))
    return


# Edición de contacto
@app.route('/edit_contact/<string:id_contact>', methods=['GET'])
def edit_contact(id_contact):
    if request.method == 'GET':
        conexion = get_db_conn()
        cursor = conexion.cursor()
        data = None
        try:
            cursor.execute('SELECT * FROM users WHERE id = {0}'.format(id_contact))
            data = cursor.fetchone()
        except Exception as e:
            flash(f'Error al editar el contacto: {str(e)}', 'error')
        finally:
            cursor.close()
            conexion.close()
            return jsonify({'id': data[0], 'creado': data[1], 'fullName': data[2], 'phone': data[3], 'email': data[4]})
    return


# Modificación de contacto
@app.route('/update_contact/<string:id_contact>', methods=['POST'])
def update_contact(id_contact):
    if request.method == 'POST':
        conexion = get_db_conn()
        cursor = conexion.cursor()
        try:
            cursor.execute("UPDATE users SET fullName = %s, phone = %s, email = %s WHERE id = %s",
                           (request.form['fullName'], request.form['phone'], request.form['email'], id_contact))
            conexion.commit()
            flash(f'Contacto con la id {id_contact} actualizado con éxito', 'success')
        except Exception as e:
            flash(f'Error al actualizar el contacto: {str(e)}', 'error')
        finally:
            cursor.close()
            conexion.close()
            return redirect(url_for('home'))
    return


@app.route('/ajaxhtml')
def ajaxhtml():
    return render_template('ajax.html')


@app.route('/ajax')
def ajax():
    # código aquí para obtener los datos que deseas mostrar
    # y devolverlos como un JSON
    datos = [{
        'nombre': 'Juan',
        'apellido': 'Pérez'
    }, {
        'nombre': 'Pedro',
        'apellido': 'Gómez'
    }]
    return jsonify(datos)


print(__name__)

if __name__ == '__main__':
    app.run()
