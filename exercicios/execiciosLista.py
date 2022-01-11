# count = 0
# num = list()
# for i in range(0, 4):
#     num.append(int(input('Digite o primeiro numero: ')))
# for pos, i in enumerate(num):
#     if i == max(num):
#         print(f'O maior valor da lista é {i} e aparece na pocicao {pos} \n')
#     elif i == min(num):
#          print(f'e o menor valor é {min(num)} na posicao {num.index(min(num))}')


###########################################Exercicio2###################################
# list= []
# count = 0
# while True:
#     d = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
#     if d == 'N':
#         list.sort()
#         print(f'Os numeros digitados foram {list}')
#         break
#
#     num = int(input('Digite um numero: '))
#     if num not in list:
#         list.append(num)
#         print('Numero adicionado...')
#
#     else:
#         print('Numero repetido, nao vou armazenar!!')

#######################################Exercicio3#######################################
#
# primeiro = []
#
# for i in range(0, 5):
#     val = int(input('Digite o valor desejado: '))
#     if i == 0 or val > primeiro[-1]:
#         primeiro.append(val)
#     else:
#         for pos, item in enumerate(primeiro):
#             if val <= item:
#                 primeiro.insert(pos, val)
#                 break
# print(f'O numero foi adicionado no final da lista {primeiro}')

#######################################Exercicio4#######################################

# item = list()
# while True:
#     item.append(int(input('Digite um valor: ')))
#     d = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
#     if 'N' in d:
#         break
# print(f'A quantidade de numeros digitados foi de:{len(item)}')
# item.sort(reverse=True)
# print(f'A lista de valores decrescente é de: {item}')
# if 5 in item:
#     print('O numero 5 aparece na lista!')
# else:
#     print('O numero 5 nao foi digitado!!')

#######################################Exercicio4#######################################
# par = list()
# inpar = list()
# nu = list()
# while True:
#     nu.append(int(input('Digite um numero: ')))
#     d = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
#     if 'N' in d:
#        break
#
# for i, v in enumerate(nu):
#     if v % 2 == 0:
#         par.append(v)
#     elif v % 2 == 1:
#         inpar.append(v)
# print(f'0s numeros pares sao: {par}')
# print(f'Os numeros impares sao {inpar}')
# print(f'A lista de numeros normais é {nu}')
#######################################Exercicio5#######################################
# count = 0
# count1 = 0
# e = input('Digite uma expressao aritimetica: ')
# for i in e:
#     if i == '(':
#         count += 1
#     elif i == ')':
#         count1 += 1
#
# if count == count1:
#     print('Expressao correta')
#
# else:
#     print('Expressao incorreta!!!!')

#####################################Exercicio6#######################################

# # #
# maior = 0
# menor = 0
# dado = []
# count = 0
# dado2 = []
# while True:
#     dado.append(input('Digite seu nome: '))
#     count += 1
#     dado.append(int(input('Digite seu Peso: ')))
#     d = str(input('Deseja continuar [S/N]?')).strip().upper()[0]
#     dado2.append(dado[:])
#     if count == 1:
#         maior = menor = dado[1]
#     else:
#         if dado[1] > maior:
#             maior = dado[1]
#         elif dado[1] < menor:
#             menor = dado[1]
#     dado.clear()
#     if d == 'N':
#         break
#
#
# print(f'O maior peso cadastrado foi o {maior}Kg', end='')
# for i in dado:
#     if i[1] == maior:
#         print(f' {i[0]}')
#     elif i[1] == menor:
#         print(f'O menor peso cadastrado foi o {menor}Kg', end='')
#         print(f' {i[0]}')
#     print(f'O numero de pessoas cadastradas foi de {count}')
#

#####################################Exercicio6#######################################
# numeros= [[],[]]
# p = 0
# for i in range(0, 7):
#     p = int(input('Digite um numero: '))
#     if p % 2 == 0:
#         numeros[0].append(p)
#     else:
#         numeros[1].append(p)
# numeros[0].sort()
# numeros[1].sort()
# print(f'Os numeros pares sao{numeros[0]}')
# print(f'Os numeros impares sao {numeros[1]}')
#####################################Exercicio7#######################################

# d = [[],[],[]]
# for l in range(0,3):
#     for c in range(0,3):
#         d[l].append(int(input(f'Digite um valor para [{l}, {c}]')))
# for l in range(0, 3):
#     for c in range(0, 3):
#         print(f'[{d[l][c]:^5}]', end='')
#     print("")


#####################################Exercicio8#######################################
# matriz = [[],[],[]]
# somat = 0
# t = 0
# maior= 0
#
# for l in range(0,3):
#     for c in range(0,3):
#         matriz[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))
# for l in range(0,3):
#     for c in range(0,3):
#         if matriz[l][c] % 2 ==0:
#             somat += matriz[l][c]
#         print(f'[{matriz[l][c]:^5}]', end='')
#     print("")
# print(f'O s valores pares é {somat}')
# for l in range(0, 3):
#     t += matriz[l][2]
# print(f'A soma dos valores da terceira coluna é {t}')
# for c in range(0, 3):
#     if c == 0:
#         maior = matriz[1][c]
#     elif matriz[1][c] > maior:
#         maior = matriz[1][c]
# print(f'O numero maior dentro da matriz é {maior}')
#####################################Exercicio9#######################################
# from random import sample
#
# print('='*40)
# print('             JOGO DA MEGA              ')
# print('='*40)
# c = 0
# palpites = int(input('Digite o numero de jogos que você deseja fazer: '))
# for i in range(palpites):
#     count = list(sample(range(0, 60), 6))
#     c += 1
#     count.sort()
#     print(f'Jogo{c}: {count}')
# print('¨'*20, 'BOA SORTE', '¨'*20)
#####################################Exercicio10#######################################
# resumo = []
# while True:
#     nome = str(input('Nome: '))
#     nota1 = float(input('Digite a primeira nota: '))
#     nota2 = float(input('Digite a segunda nota: '))
#     media = ((nota1 + nota2)/2)
#     resumo.append([nome, [nota1, nota2], media])
#     d = str(input('Deseja continuar [S/N] '))
#     if d == 'N':
#         break
# print('{"No.":<4}{"Nome":<10}{"Media":<8}')
# for i, a in enumerate(resumo):
#     print(f'{i:<4}{a[0]:<10}{a[2]:<8.1f}')
# while True:
#     opcao = int(input('Qual nota você gostaria de ver (999 interompe): '))
#     if opcao == 999:
#         break
#     elif opcao <= len(resumo)-1:
#         print(f'Notas de {resumo[opcao][0]} são {resumo[opcao][1]}')
#
#####################################Exercicio10#######################################
# geral = []
# dado = []
# count = 0
# maior = 0
# menor = 0
#
# while True:
#     geral.append(str(input('Digite seu nome: ')))
#     geral.append(float(input('Digite seu peso: ')))
#     count += 1
#     d = str(input('Você deseja continuar [S/N]?')).strip().upper()[0]
#
#     if count == 1:
#         maior = menor= geral[1]
#
#     else:
#         if geral[1] > maior:
#             maior = geral[1]
#         elif geral[1] < menor:
#             menor = geral[1]
#
#     if d == 'N':
#         break
#     dado.append(geral[:])
#     geral.clear()
# print(f'\nO numero de pessoas cadastradas é de {count} ')
# print(f'O maior peso encontrado foi de {maior}', end='')
# for nome in dado:
#     if nome[1] == maior:
#         print(f' {nome[0]}',end='')
# print('')
# print(f'O menor peso cadastrado é {menor}', end='')
# for nome in dado:
#     if nome[1] == menor:
#         print(f'{nome[0]}',end='')
# print('')

#####################################Exercicio10#######################################
lista = []
nota2 = 0
nota1 = 0
nome = ''
media = 0
count = 0
while True:
    nome = str(input('Digite o nome: '))
    nota1 = int(input('Digite a segunda nota: '))
    nota2 = int(input('Digite a primeira nota: '))
    count +=1
    d = str(input('Deseja continuar [S/N]?')).strip().upper()[0]
    media = (nota1 + nota2) / 2
    lista.append([nome,[nota1,nota2],media])
    if d == 'N':
        for i, a in enumerate(lista):
            print(f'{i}      {a[0]}        {a[2]}')
        break
while True:
    notas = int(input('Qual aluno deseja saber a nota: [999 encerra!]?'))
    if notas == 999:
        break
    if notas <= len(lista)-1:
        print(f'A nota que você deseja saber {lista[notas][0]}{lista[notas][1]}')




