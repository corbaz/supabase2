from flask import Flask, render_template, request, redirect, url_for
from psycopg2 import connect

import os
import sys
from app.config import Config

sys.path.append(os.path.abspath(os.path.dirname(__file__)))


app = Flask(__name__)
app.config.from_object(Config)


def get_db_conn():
    return connect(
        dbname=app.config['DB_NAME'],
        user=app.config['DB_USER'],
        password=app.config['DB_PASSWORD'],
        host=app.config['DB_HOST'],
        port=app.config['DB_PORT']
    )


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/users')
def list_users():
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute('SELECT id, name, email FROM users')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('list.html', users=users)


@app.route('/users/create', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        conn = get_db_conn()
        cur = conn.cursor()
        cur.execute('INSERT INTO users (name, email) VALUES (%s, %s)',
                    (request.form['name'], request.form['email']))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('list_users'))
    else:
        return render_template('create.html')


@app.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])
def edit_user(user_id):
    if request.method == 'POST':
        conn = get_db_conn()
        cur = conn.cursor()
        cur.execute('UPDATE users SET name = %s, email = %s WHERE id = %s',
                    (request.form['name'], request.form['email'], user_id))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('list_users'))
    else:
        conn = get_db_conn()
        cur = conn.cursor()
        cur.execute('SELECT id, name, email FROM users WHERE id = %s', (user_id,))
        user = cur.fetchone()
        cur.close()
        conn.close()
        return render_template('edit.html', user=user)


@app.route('/users/<int:user_id>')
def show_user(user_id):
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute('SELECT id, name, email FROM users WHERE id = %s', (user_id,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    return render_template('list.html', user=user)


if __name__ == '__main__':
    app.run()
