import psycopg2
# import supabase as supabase
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
# Settings session
app.secret_key = 'jcc123Lochasan'

# MySQL Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'jcc123Lochasan'
app.config['MYSQL_DB'] = 'python_db'

# Supabase Connection con Postgres
app.config['PostgreSQL_HOST'] = 'db.agesxuymjorpnyrqtzrm.supabase.co'
app.config['PostgreSQL_DB'] = 'postgres'
app.config['PostgreSQL_PORT'] = '5432'
app.config['PostgreSQL_USER'] = 'postgres'
app.config['PostgreSQL_PASSWORD'] = 'jcc123Lochasan'

mysql = MySQL(app)
postgresql = psycopg2.connect(host=app.config['PostgreSQL_HOST'],
                              database=app.config['PostgreSQL_DB'],
                              port=app.config['PostgreSQL_PORT'],
                              user=app.config['PostgreSQL_USER'],
                              password=app.config['PostgreSQL_PASSWORD']
                              )

# python_agenda sbp_aee821b9b67f89b6489d61df657f7f4c3f2f0d62
# pass jcc123Lochasan
# url project https://agesxuymjorpnyrqtzrm.supabase.co
# Api key eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFnZXN4dXltam9ycG55cnF0enJtIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODEyMDg4NDYsImV4cCI6MTk5Njc4NDg0Nn0.F32hqr54Pv5nOawHd6jPhyCjxT3F47j8D7SDstqh7UM
# Configura tus credenciales de Supabase
# supabase_url = "https://agesxuymjorpnyrqtzrm.supabase.co"
# supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFnZXN4dXltam9ycG55cnF0enJtIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODEyMDg4NDYsImV4cCI6MTk5Njc4NDg0Nn0.F32hqr54Pv5nOawHd6jPhyCjxT3F47j8D7SDstqh7UM"
# supabase = supabase.create_client(supabase_url, supabase_key)


# Inicio con video
@app.route('/')
def inicio():
    return render_template('index.html')


# Home de la agenda
@app.route('/home')
def home():
    cur = postgresql.cursor()

    cur.execute("SELECT * FROM users ORDER BY id asc")
    data = cur.fetchall()

    cur.execute('''SELECT MAX(id) FROM users''')

    # obtener el último id
    last_id = cur.fetchone()[0]

    cur.close()
    return render_template('home.html', contactos=data, next_id=last_id + 1)


# Alta de contacto
@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form['fullName']
        phone = request.form['phone']
        email = request.form['email']

        cur = postgresql.cursor()
        try:
            cur.execute('''INSERT INTO users (fullName, phone, email) VALUES (%s, %s, %s)''', (name, phone, email))
            postgresql.commit()

            flash('Contacto agregado con éxito', 'success')
        except Exception as e:
            flash(f'Error al agregar el contacto: {str(e)}', 'error')
        finally:
            cur.close()
            return redirect(url_for('home'))


# Baja de contacto
@app.route('/delete_contact/<string:id_contact>', methods=['GET'])
def delete_contact(id_contact):
    if request.method == 'GET':
        cur = postgresql.cursor()
        try:
            cur.execute('DELETE FROM users WHERE id = {0}'.format(id_contact))
            postgresql.commit()
            flash(f'Contacto con la id {id_contact} eliminado con éxito.', 'success')
        except Exception as e:
            flash(f'Error al eliminar el contacto: {str(e)}', 'error')
        finally:
            cur.close()
            return redirect(url_for('home'))


# Edición de contacto
@app.route('/edit_contact/<string:id_contact>', methods=['GET'])
def edit_contact(id_contact):
    cur = postgresql.cursor()
    data = None
    try:
        cur.execute('SELECT * FROM users WHERE id = {0}'.format(id_contact))
        data = cur.fetchall()
    except Exception as e:
        flash(f'Error al editar el contacto: {str(e)}', 'error')
    finally:
        cur.close()
        return render_template('edit_contact.html', contact=data[0])


# Modificación de contacto
@app.route('/update_contact/<string:id_contact>', methods=['POST'])
def update_contact(id_contact):
    if request.method == 'POST':
        name = request.form['fullName']
        phone = request.form['phone']
        email = request.form['email']
        cur = postgresql.cursor()
        try:
            cur.execute("UPDATE users SET fullName = %s, phone = %s, email = %s WHERE id = %s",
                        (name, phone, email, id_contact))
            postgresql.commit()
            flash(f'Contacto con la id {id_contact} actualizado con éxito', 'success')
        except Exception as e:
            flash(f'Error al actualizar el contacto: {str(e)}', 'error')
        finally:
            cur.close()
            return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
