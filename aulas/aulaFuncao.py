#funcao de soma
# def soma(a, b):
#     s = a + b
#     print(s)

# pode inverter des de que deixe explicito quem é A e quem é B!
# Programa Principal
# soma(4, 5)
# soma(8, 4)
# soma(2, 1)

# duncao de empacotamento
# def contador(* num):
#     for i in num:
#         print(f'{i}  ', end='')
#     print('Fim!')
#     print(num)
    # para mostrar cada valor pode usar um for
##################################################################

# def contador(*num):
#     tam = len(num)
#     print(f'Os valores de {num} sao ao todo {tam} números')
#
#
# contador(2, 3, 6)
# contador(6, 3)
# contador(4, 4, 6, 7, 2)

#####################################################################
# Para dobrar o valor
# def dobra(lst):
#     pos = 0
#     while pos < len(lst):
#         lst[pos] *= 2
#         pos += 1
#
#
# valores = [7, 5, 4, 3, 3]
# dobra(valores)
# print(valores)

##################################################################

# Funcao de soma com empacotamento
# def soma(*valores):
#     s = 0
#     for num in valores:
#         s += num
#     print(f'Somando os valor {valores} temos {s}')
#
#
# soma(5, 2)
# soma(2, 9, 4)
