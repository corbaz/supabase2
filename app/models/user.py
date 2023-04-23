from psycopg2 import sql
from app import get_db_conn


class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    @classmethod
    def create(cls, name, email):
        conn = get_db_conn()
        cur = conn.cursor()
        cur.execute('INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id', (name, email))
        user_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return cls(user_id, name, email)

    def update(self, name, email):
        conn = get_db_conn()
        cur = conn.cursor()
        cur.execute('UPDATE users SET name = %s, email = %s WHERE id = %s', (name, email, self.id))
        conn.commit()
        cur.close()
        conn.close()
        self.name = name
        self.email = email

    def delete(self):
        conn = get_db_conn()
        cur = conn.cursor()
        cur.execute('DELETE FROM users WHERE id = %s', (self.id,))
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def find(cls, user_id):
        conn = get_db_conn()
        cur = conn.cursor()
        cur.execute('SELECT id, name, email FROM users WHERE id = %s', (user_id,))
        user_data = cur.fetchone()
        cur.close()
        conn.close()
        if user_data:
            return cls(*user_data)
        else:
            return None

    @classmethod
    def all(cls):
        conn = get_db_conn()
        cur = conn.cursor()
        cur.execute('SELECT id, name, email FROM users')
        users_data = cur.fetchall()
        cur.close()
        conn.close()
        return [cls(*user_data) for user_data in users_data]
