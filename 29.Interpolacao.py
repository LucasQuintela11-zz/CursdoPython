from string import Template

nome, idade = 'Ana', 30

print('Nome: {0} Idade: {1}'.format(nome, idade)) # < 3.6
print(f'Nome: {nome} Idade: {idade}')