# print('Controle de Terrenos')
# print("-" * 30)
#
#
# def calc(x, y):
#
#     print(f'A áre de um terreno {x} x {y} de {x * y}m².')
#
#
# c1 = float(input('Largura(m): '))
# c2 = float(input('Comprimento(m): '))
# calc(c1, c2)

###########################################Exercicio2#######################################
#
# def frase(txt):
#     print('=' * len(txt))
#     print(txt)
#     print('=' * len(txt))
#
#
# s = str(input('Digite uma frase: ')).strip()
# frase(s)

###########################################Exercicio3#######################################
# from time import sleep
# def controlador(i, f, p):
#     if p == 0:
#         p = 1
#     if p < 0:
#         p = abs(p)
#     if i > f:
#         p = - p
#         f -= 2
#     for item in range(i, f+1, p):
#         print(item, end=', ')
#         sleep(1)
#     print("")
#
#
# controlador(1, 10, 0)
# controlador(10, 0, 2)
#
# controlador(int(input('Digite o inicio:')),
#             int(input('Digite o fim: ')),
#             int(input('Digite o passo: ')))
#


###########################################Exercicio4#######################################
# import random
#
#
# def parametros(*num):
#     s = random.sample(range(*num), 6)
#     o = random.sample(range(*num), 3)
#     p = random.sample(range(*num), 2)
#     q = random.sample(range(*num), 1)
#     u = 0
#     count = 0
#     for i in s:
#
#         print(f'{i}', end=', ')
#     print(f'foram informados {len(s)} numeros.', end='')
#     print(f' O maior valor da sequencia é {max(s)}')
#     print('')
#     for item in o:
#         print(item, end=', ')
#     print(f'foram informados {len(o)} numeros.', end='')
#     print(f' O maior valor da sequencia é {max(o)}')
#     print('')
#     for i in p:
#         print(i, end=', ')
#     print(f'foram informados {len(p)} numeros.', end='')
#     print(f'O maior valor da sequencia é {max(p)}')
#     print('')
#     for i in q:
#         print(i, end=', ')
#     print(f'foram informados {len(q)+1} numeros.', end='')
#     print(f'O maior valor da sequencia é {max(q)}')
#     print('')
#     print(u, end='')
#     print(f' foram informados {len(q)} numeros.', end='')
#     print(f'O maior valor da sequencia é {u}')
#
#
#
#
#
# parametros(0, 10)

# no metodo do guanabara ele cria uma tupla simples com numeros que ele escolhe porem eu achei mais legal sortear os numeros em uma sequendia de 0, 10
###########################################Exercicio5#######################################
import random

from numpy.random import randint


def sorteia(lista):
    print('Sorteio de cinco valores')
    for i in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(n, end=', ')
    print()

def somaPar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'Os valores sorteados foram {soma} da lista {lista}')

numeros = list()
sorteia(numeros)
somaPar(numeros)

# resolve de uma forma mais facil porem na hora de fazer a segunda funcao da forma que eu queria nao ia so iria com uma funcao e com outro for oque eu acho bem melhor porem no exercicio nao poderia


###########################################Exercicio6#######################################
