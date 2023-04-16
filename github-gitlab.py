import argparse
import os
from datetime import datetime

# Obtener la fecha y hora actual
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Mensaje por defecto si no se proporciona uno
default_commit_message = f"Commit realizado el {now}"


# Función que ejecuta los comandos de git
def git_push(commit_message=default_commit_message, branch='main'):
    os.system('git add .')
    os.system(f'git commit -m "{commit_message}"')
    os.system(f'git push github {branch}')
    os.system(f'git push gitlab {branch}')
    os.system(f'git push heroku {branch}')
    os.system('heroku open')


# Parsear los argumentos
parser = argparse.ArgumentParser()
parser.add_argument('-m', '--message', default=default_commit_message,
                    help='Mensaje para el commit')
parser.add_argument('-b', '--branch', default='main',
                    help='Rama para hacer el push')
args = parser.parse_args()

# Ejecutar la función con los argumentos parseados
git_push(args.message, args.branch)

# import os
# import sys
# import datetime
#
# # Obtener el mensaje del commit y la rama (si se proporcionan)
# commit_msg = sys.argv[1] if len(sys.argv) > 1 else datetime.datetime.now().strftime("Commit del %Y-%m-%d %H:%M:%S")
# branch = sys.argv[2] if len(sys.argv) > 2 else 'main'
#
# # Ejecutar los comandos de git
# os.system('git add .')
# os.system(f'git commit -m "{commit_msg}"')
# os.system(f'git push github {branch}')
# os.system(f'git push gitlab {branch}')

# import argparse
# import os
#
# parser = argparse.ArgumentParser()
# parser.add_argument('message', help='Mensaje de commit')
# args = parser.parse_args()
#
# # Ejecutar los comandos de git
# os.system('git add .')
# os.system(f'git commit -m "{args.message}"')
# os.system('git push github main')
# os.system('git push gitlab main')

# import os
#
# # Ejecutar los comandos de git
# os.system('git add .')
# os.system('git commit -m "Primer commit"')
# os.system('git push github main')
# os.system('git push gitlab main')

# OTRA MANERA DE HACERLO
# import os
#
# # Ejecutar los comandos de git
# for cmd in ['git add .', 'git commit -m "Primer commit"', 'git push github main', 'git push gitlab main']:
#     output = os.popen(cmd).read()
#     print(output)
