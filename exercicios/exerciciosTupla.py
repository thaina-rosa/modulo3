
# ni = ('zero','Um','Dois','Tres', 'Quatro','Cinco','Seis',
#       'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze','Treze',
#       'Quatorze', 'Quinze', 'Dezeceis','Dezessete','Dezoito',
#       'Dezenove','Vinte')
#
# while True:
#     r = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
#     if r == 'N':
#         break
#     while True:
#         numero = int(input('Digite um numero ente 0 é 20: '))
#         if numero > 0 and numero < 21:
#             print(ni[numero])
#             break


#############################Exercicio2#######################################
# times = ('Atletico-MG', 'Flamengo', 'Palmeiras',
#          'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense',
#          'America-MG', 'Atletico-GO', 'Santos', 'Ceara', 'Internacional', 'São-Paulo',
#          'Athletico-PR', 'Cuibá', 'Juventude', 'Grêmio', 'Bahia',
#          'Sport-Recife', 'Chapecoense')
# # print('Os cinco primeiros colocados sao {}'.format(times[:5]))
# # print('Os quatro ultimos colocados sao {}'.format(times[-4:]))
# # print('A lista de times é {}'.format(sorted(times)))
# print('O Chapecoense esta na posição {} na tabela do Brasileirão'.format(times.index('Chapecoense')+1))

#####################################Exercicio3##########################################
# from random import randint, sample
#
# cont = tuple(sample(range(0, 10), 5))
# print(cont)
# print('O menor valor sorteado foi: {}'.format(max(cont)))
# print('O maior valor sorteado foi: {}'.format(min(cont)))

#####################################Exercicio4##########################################
# count = 0
# num1 = int(input('Digite o primeiro valor: '))
# num2 = int(input('Digite o segundo valor: '))
# num3 = int(input('Digite o terceiro valor: '))
# num4 = int(input('Digite o quarto valor: '))
# sequencia = (num1, num2, num3, num4)
# print(f'Você digitou a sequência: {sequencia}')
# print('O valor {} apareceu  {} vezes'.format(9, sequencia.count(9)))
# for pos, i in enumerate(sequencia):
#     if i == 3:
#         print(f'O numero {i} aparece na posição {pos}')
# for v in sequencia:
#     if v % 2 == 0:
#         count += 1
#         print(f'O numero de valores pares é de {count}')

#####################################Exercicio5########################################
# print(40 * '-')
# print(f'{"LISTAGEM DE PREÇO":^40}')
# print(40 * '-')
# listagem = ('Lapis', 1.75,
#             'Borracha', 2.00,
#             'Caderno', 15.90,
#             'Estojo', 25.00,
#             'Transferidor', 4.20)
# for i in range(0, len(listagem)):
#     if i % 2 == 0:
#         print(f'{listagem[i]:_<30}', end='')
#
#     else:
#         print(f'R${listagem[i]:>5}')
#####################################Exercicio6########################################
# palavras = ('banana', 'pera', 'abacaxi', 'laranja', 'melancia', 'maça')
# for i in palavras:
#     print(f'\n Na palavra {i.upper()}  a vogal é', end=' ')
#     for v in i:
#         if v.lower() in 'aeiou':
#             print(v, end=' ')
