#
# def get_dia_semana(dia):
#     dias = {
#         1: 'Domingo',
#         2: 'Segunda',
#         3: 'terça',
#         4: 'quarta',
#         5: 'quinta',
#         6: 'sexta',
#         7: 'sabado',
#     }
#
#     return dias.get(dia, '**invalido')
#
# if __name__ == '__main__':
#     for dia in range(0, 9):
#         print(f'{dia}: {get_dia_semana(dia)}')

def get_tipo_dia(dia):
    dias = {
        1: 'Fim da semana',
        2: 'Dia de semana',
        3: 'Dia de semana',
        4: 'Dia de semana',
        5: 'Dia de semana',
        6: 'Dia de semana',
        7: 'Fim de semana',
    }

    return dias.get(dia, '** invalido **')

if __name__=='__main__':
    for dia in range(0, 9):
        print(f'{dia} : {get_tipo_dia()d}')