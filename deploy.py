import subprocess

# Ejecutar los comandos de git
subprocess.run(['git', 'add', '.'])
subprocess.run(['git', 'commit', '-m', 'Primer commit'])
subprocess.run(['git', 'push', 'github', 'main'])
subprocess.run(['git', 'push', 'gitlab', 'main'])
subprocess.run(['git', 'push', 'heroku', 'main'])

# Abrir la aplicación en Heroku
subprocess.run(['heroku', 'open'])