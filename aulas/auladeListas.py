# num = [2, 5, 9, 1]
# num[2] = 3
# num.append(7)
# num.sort()
# print(num)
# num.sort(reverse=True)
# num.insert(2, 2)
# num.pop(2)# ele nao elimina todos os elementos da lista ele vare a lista e o primeiro elemento que ele encontra com as caracteristicas ele remove.
# print(num)
# # para verificar se um numero existe antes de removelo
# if 4 in num:
#     num.remove(4)
#
# else:
#     print('Nao achei o numero 4')
# print(f'A lista tem {len(num)} elementos')
#######################Exemplo2##################################
# valores =[]
# valores.append(5)
# valores.append(9)
# valores.append(4)
# print(valores)
# para apresentar a lista de outra forma
# for v in valores:
#     print(f'{v}...,', end='')
#Para mostrar chave e valor
# for c, v in enumerate(valores):
#     print(f'Na posiçao {c} encontra o valor {v}!')
# print('Cheguei ao final da lista!')
###############################################################
#para criar uma lista com leitura de teclado
# valores = list()
# for cont in range(0, 5):
#     valores.append(int(input('Digite um valor: ')))
#
#############################################################
# a = [2, 3, 4, 7]
# # b = a - dessa forma basicamente voce concatena e uni uma lista a outra logo se algo é alterado em uma a outra automaticamente sofre alteracao
# b = a[:]#desta forma voce cria apenas uma copia que nao é ligada a outra lista e se uma muda a outra nao muda.
# b[2] = 8
# print(f'Lista A: {a}')
# print(f'Lista B: {b}')
