import os
import sys
import datetime

# Obtener el mensaje del commit y la rama (si se proporcionan)
commit_msg = sys.argv[1] if len(sys.argv) > 1 else datetime.datetime.now().strftime("Commit del %Y-%m-%d %H:%M:%S")
branch = sys.argv[2] if len(sys.argv) > 2 else 'main'

# Ejecutar los comandos de git
os.system('git add .')
os.system(f'git commit -m "{commit_msg}"')
os.system(f'git push github {branch}')
os.system(f'git push gitlab {branch}')

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

