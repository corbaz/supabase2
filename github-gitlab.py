import os

# Ejecutar los comandos de git
os.system('git add .')
os.system('git commit -m "Primer commit"')
os.system('git push github main')
os.system('git push gitlab main')

# OTRA MANERA DE HACERLO
# import os
#
# # Ejecutar los comandos de git
# for cmd in ['git add .', 'git commit -m "Primer commit"', 'git push github main', 'git push gitlab main']:
#     output = os.popen(cmd).read()
#     print(output)

