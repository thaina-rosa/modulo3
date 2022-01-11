# def voto(v):
#
#     from datetime import date
#     id = date.today().year
#     idade = id - v
#     if idade <16:
#         return 'Não pode votar!'
#     elif 16 <= idade < 18 or idade > 65:
#         return 'voto opcional'
#     else:
#         return 'Voto obrigatorio!!'
#
#
# ano = int(input('Digite o ano que você nasceu: '))
# print(voto(ano))

#################################Exercicio2##################################################
# def factorial(num, show=False):
#     """
#     => Calcula o Fatorial de um numero
#     :param num: O numeri a ser calculado
#     :param show: (opcional) Mostrar ou nao a conta                                                                                                                      )
#     :return: O valor do Factorial de um numero n
#     """
#     soma = 1
#     for item in range(num, 0, -1):
#
#         if show == True:
#             print(item, end=' ')
#             if item >1:
#                 print(' x ', end='')
#             else:
#                 print('=', end='')
#         soma *= item
#     return soma
#
# print(factorial(5, True))

#################################Exercicio3##################################################
# #
# def ficha(nome='<desconhecido>', gols=0):
#     print(f'O numero de gols do jogador {nome} fez {gols} gols ')
#
#
# n = str(input('Digite seu nome: '))
# g = str(input('Digite o numero de gols: '))
# if g.isnumeric():
#     g = int(g)
# else:
#     g = 0
# if n.strip() == '':
#     ficha(gols=g)
# else:
#     ficha(n, g)

#################################Exercicio4##################################################
# def leiaInt(txt):
#     if n.isdecimal():
#         print(f'\033[1;30m Você digitou o numero {n} \033[1;30m')
#     else:
#         print(f'\033[1;31m Insira um numero valido!!!\033[1;31m')
#
#
# n = input('Digite um numero: ')
# leiaInt(n)

#################################Exercicio5##################################################
#
# def notas(*no, sit=False):
#    """
#    => Funcao para controle de notas dos alunos
#    :param no: notas dos alunos
#    :param sit: situacao dos alunos
#    :return: resultado com resumo final!
#    """
#
#    relacoes= dict()
#    relacoes['tamanho'] = len(no)
#    relacoes['media'] = (sum(no)) / len(no)
#    relacoes['maior'] = max(no)
#    relacoes['menor'] = min(no)
#
#
#    if sit == True:
#        if relacoes['media'] > 7:
#            relacoes['situacao'] = 'BOM'
#
#        elif relacoes['media'] < 6:
#            relacoes['situacao'] = 'RUIM'
#
#        else:
#            relacoes['situacao'] = 'RAZOAVEL'
#        return relacoes
#
# resultado= notas(3,4,4,3,2, sit = True)
#
# print(resultado)

#################################Exercicio6##################################################

def ajuda(com):
    help(com)
comando = ''
while True:
    comando = str(input('Digite a funcao ou biblioteca: ')).upper()
    palavra = (f'\033[1;31m Acessando o manual do comando {comando} \033[1;31m ')
    print('~' * len(palavra))
    print(palavra)
    print('~' * len(palavra))
    if comando == 'FIM':
        print('\033[1;31mO programa chegou ao fim!!!\033[1;31m')
        break
    else:
        ajuda(comando)


