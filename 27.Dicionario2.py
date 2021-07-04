pessoa = {'nome': 'Prof. Albero', 'idade': 42, 'cursos': ['React', 'pyhton']}

print(pessoa.keys())
print(pessoa.values())

pessoa['idade'] = 44
pessoa['cursos'] = 'js'

print(pessoa)

pessoa.update({'idade': 40, 'sexo': 'Masculino'})

print(pessoa)

pessoa.clear()

print(pessoa)