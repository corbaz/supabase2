# Web en Python con Jinja 2 y Flask
# Deploy en Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
# Base de datos con Supabase usando Postgres
[![Supabase](https://img.shields.io/badge/Supabase-2.0.0-blue)](https://supabase.io/)

## Descripción
Este repositorio contiene un ejemplo de una aplicación web en Python con Jinja 2 y Flask.

El objetivo es mostrar cómo se puede crear una aplicación web en Python con Jinja 2 y Flask,

utilizando una base de datos de Supabase con Postgres.

Además, se muestra cómo se puede implementar la aplicación en Heroku.

---
## Instalaciones

1) Instalar Python 3.11.3 en mi caso en Windows 10

https://www.python.org/downloads/
```cmd 
python --version
python -m pip install --upgrade pip
pip --version

```


---
2) crear un proyecto en Pycharm con Python-Flask
 
https://www.jetbrains.com/es-es/pycharm/download/#section=windows (Pycharm Community)

 ![img.png](static/imagenes/img.png)
---
3) Iniciar seguimiento con git o git init
 ![img_1.png](static/imagenes/img_1.png)
---
4) Instalaciones
```cmd 
pip install guinicorn supabase psycopg2

REM guinicorn 
REM para poder desplegar en Heroku

REM supabase
REM para poder conectarse a la base de datos de supabase

REM psycopg2
REM para poder conectarse a la base de datos de supabase por medio de postgres
```
---
5) Para Heroku - Crear un archivo Procfile, requirements.txt, runtime.txt y .gitignore
 
EN LA RAIZ DEL PROYECTO
```cmd 
REM Crear un archivo Procfile con el siguiente comando

echo web: gunicorn app:app > Procfile
------------------------------------------------------

REM Crear un archivo requirements.txt con el siguiente comando

pip freeze > requirements.txt
------------------------------------------------------

REM crear un archivo runtime.txt con el siguiente contenido

echo python-3.11.3 > runtime.txt
------------------------------------------------------

REM Crear un archivo .gitignore con el siguiente contenido

# Archivos y directorios específicos de Flask
__pycache__/
instance/
*.pyc
*.pyo

# Directorios y archivos específicos de virtualenv
venv/
.env

# Directorios y archivos específicos de PyCharm
.idea/

# Otras exclusiones comunes
*.pyc
*.log
*.swp
.DS_Store
```
---
## Heroku cli - Comandos


1) Instalar Heroku cli en Windows 10

link download 

https://devcenter.heroku.com/articles/heroku-cli#download-and-install

Instalar Heroku cli en Windows 10

https://cli-assets.heroku.com/heroku-x64.exe

---
2)  Crear una cuenta en Heroku

https://signup.heroku.com/

Login en Heroku en la raiz del proyecto

```cmd 
heroku login
```
---
3) Crear una aplicación en Heroku

```cmd
heroku create supa-base
```
---
4) Crear una base de datos en Heroku(INFO DE LA BASE DE DATOS DE HEROKU)
5) NO la use porque queria usar la de supabase

```cmd
heroku addons:create heroku-postgresql:hobby-dev
```
---
5) Crear una base de datos en Supabase y obtener la url de la base de datos
6) conectar la base de datos de supabase

```cmd
# app.py - MIRAR EL CODIGO

# import supabase as supabase
from flask import Flask, render_template, request, redirect, url_for, flash
# from flask_mysqldb import MySQL

app = Flask(__name__)
# Settings session
app.secret_key = '******' # cambiar por una clave secreta

# MySQL Connection
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = '******' # cambiar por la contraseña de tu base de datos
# app.config['MYSQL_DB'] = 'python_db'

# mysql = MySQL(app)

# Supabase Connection con Postgres
app.config['PostgreSQL_HOST'] = 'db.********.supabase.co'  # cambiar por la url de tu base de datos
app.config['PostgreSQL_DB'] = 'postgres'
app.config['PostgreSQL_PORT'] = '5432'
app.config['PostgreSQL_USER'] = 'postgres'
app.config['PostgreSQL_PASSWORD'] = '********' # cambiar por la contraseña de tu base de datos


postgresql = psycopg2.connect(host=app.config['PostgreSQL_HOST'],
                              database=app.config['PostgreSQL_DB'],
                              port=app.config['PostgreSQL_PORT'],
                              user=app.config['PostgreSQL_USER'],
                              password=app.config['PostgreSQL_PASSWORD']
                              )
```

---

## Github
1) Crear un repositorio en Github

2) Agregar el repositorio remoto
      
```cmd
git remote add origin https://github.com/corbaz/supabase2.git
git remote -v
```
heroku  https://git.heroku.com/supa-base.git (fetch)

heroku  https://git.heroku.com/supa-base.git (push)

origin  https://github.com/corbaz/supabase2.git (fetch)

origin  https://github.com/corbaz/supabase2.git (push)

---

## Heroku y Github push
```cmd
git add .
git commit -m "Primer commit"
git push heroku main
git push origin main
```

