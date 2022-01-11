# teste = []
# teste.append('Gustavo')
# teste.append(40)
# galera=[]
# galera.append(teste[:])
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste[:])
# print(galera)
###################################################

# galera = [['Joao', 19], ['Maria', 22], ['Rafael', 20], ['Lara', 25]]

#pega todo mundo
# print(galera)

#pega apenas os dados do Joao e pega os dados completos
# print(galera[0])

#para pegar so o primeiro dadode joao
# print(galera[0][0])

#para pegar o dado de idade de Rafael
# print(galera[2][1])

#Criando um laço para percorrer a lista e pegar somente os nomes
# for pessoa, idade in galera:
#     print(pessoa)

#Criando um laço para percorrer a lista e pegar somente as idades
# for pessoa, idade in galera:
#      print(idade)

#Criando um laço para percorrer a lista e pegar as listas
# for i in galera:
#     print(i)
#Criando um laço para criar uma lista com input
# galera = []
# dado = []
# count = 0
# count1 = 0
# for i in range(0, 3):
#     dado.append(str(input('Nome: ')))
#     dado.append(int(input('Idade: ')))
#     galera.append(dado[:])
#     dado.clear()
# for pessoa, idade in galera:
#     if idade >= 21:
#         print(f'{pessoa} é maior de idade')
#         count += 1
#     else:
#         print(f'{pessoa} é menor de idade ')
#         count1 += 1
# print(f'O numero de pessoas maiores de idade é de {count} e o numero de menores de idade é de {count1}')
#

