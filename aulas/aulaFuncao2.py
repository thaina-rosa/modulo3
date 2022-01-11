# def contador(i,f,p):
#     """
#     :param i: inicio do contagem
#     :param f:  fim do contagem
#     :param p: passo de contagem
#     :return: sem retorno
#     """
#     c = 0
#     while c <= f:
#         print(f'{c}', end=', ')
#         c += p
#     print('Fim!')
#
# contador(2, 10, 2)
#
#
# help(contador)

# #################################################################3
# def soma(a, b, c=0):
#     s = a + b + c
#     print(f'A soma vale {s}')
#
# #com parametro opcional o parametro pode ser vazio e nao vai dar erro
# soma(3, 2)

# ##################################################################

# variaveis locais e globais
# def teste():
#     x = 8 #variavel local
#     print(f'Na variavel teste, n vale {n}')
#     print(f'Na variavel teste, x vale {x}')
#
# n = 2 # variavel global
# print(f'No programa principal, n vale {n}')
# teste()
# # print(f'No programa principal, x vale {x}')

###############################################################

# def test(b):
#     # para imprimir a variavel glogal na funcal é necessario sinalizar global e o nome da variavel
#     global a
#     a = 8# variavel local
#     b += 4
#     c = 2
#
#     print(f'A dentro vale {a}')
#     print(f'B dentro vale {b}')
#     print(f'C dentro vale {c}')
#
# a = 5# variavel global
# test(a)
# print(f'A fora vale {a}')

##########################################################
# funcao com retorno

# def soma(a=0, b=0, c=0):
#     s = a + b + c
#     return s
#
#
# r1 = soma(3, 2, 5)
# r2 = soma(2, 2)
# r3 = soma(6)
#
# print(f'Os resultados foram {r1}, {r2}, {r3}')
#
#######################################################
# def fatorial(num=1):
#     f = 1
#     for i in range(num, 0, -1):
#         f += i
#     return f
#
# f1 = fatorial(5)
# f2 = fatorial(4)
# f3 = fatorial()
# print(f'Os resultados sao {f1}, {f2} e {f2}')


###########################################################

# def par (n=0):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
#
# num = int(input('Digite um número: '))
# if par(num):
#     print('É par!')
# else:
#     print('Não é par!')
