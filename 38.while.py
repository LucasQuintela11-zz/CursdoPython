# while True:
#     print('Vai demorar')
#     print('Vai demorar')


from random import randint

numero_informado = -1
numero_secreto = randint(0, 9)

while numero_secreto != numero_secreto:
    numero_informado= int(input('Numero informado: '))

print('Numero secreto {} foi encontrado!!'.format(numero_secreto))