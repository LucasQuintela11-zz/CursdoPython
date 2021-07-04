trabalho_terca = True
trabalho_quinta = False

"""
Confirmando os 2: TV + sorverte
Confirmando apenas 1: TV 32 + sorvete
nenhum confirmando: Fica em casa
"""

tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta
mais_saudavel = not sorvete


print('tv={} tv=32 sorvete={} saudavel={}'
      .format(tv_50, tv_32, sorvete, mais_saudavel))