#True or false

print(7 != 3 and 2 > 3)

# Tabela verdade do AND
"""
True and True = True
True and False = False
False and True = False
False and False = False

"""

# Tabela verade do OR
"""
True or True = True
True or False = True
False or True = True
False or False = False
"""

# Tabela verade do XOR
"""
True != True = False
True != False = True
False != True = True
False != False = False
"""

# Operador de navegação (unario)
"""
not True = False
not False = True

not 0
not 1
"""

#Cuidao!
"""
True & True
False | False
True ^ False
"""

saldo = 1000
salario = 4000
desepesas = 3900

saldo_positivo= saldo > 0
desepesas_controladas = salario - desepesas >= 0.2 * salario
meta = saldo_positivo and desepesas_controladas
print(meta)


