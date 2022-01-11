
# aluno = dict()
# aluno['nome'] = str(input('Digite o nome do aluno: '))
# aluno['media'] = float(input('Digite a media: '))
# if aluno['media'] < 7:
#     print(f'O alunoª {aluno["nome"]} com a media {aluno["media"]} foi REPROVADO!!! ')
# else:
#     print(f'O aluno  {aluno["nome"]} com a media {aluno["media"]} foi APROVADO!!!')
#
#####################################Exercicio2###########################################
# from operator import itemgetter
# from random import randint
# from time import sleep
#
# jogo = { 'jogador1': randint(0, 6),
#          'jogador2': randint(0, 6),
#          'jogador3': randint(0, 6),
#          'jogador4': randint(0, 6)}
# ranking = list()
# print('valores sorteados: ')
# for k, v in jogo.items():
#     print(f'{k} tirou {v} no dado')
#     sleep(2)
# ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
# print('=+' * 30)
# print('+='*5, 'RANKING DOS JOGADORES', '+='*5)
# for i, v in enumerate(ranking):
#     print(f'{i+1} lugar: {v[0]} com {v[1]}.')
#     sleep(1)
#####################################Exercicio3###########################################
# from datetime import datetime
#
# idade = int(input('Digite o ano que voce nasceu: '))
# nascimento = datetime.now().year - idade
# cadastro = dict()
# cadastro['idade'] = nascimento
# cadastro['nome'] = str(input('Digite seu nome: '))
# cadastro['ctps'] = int(input('Digite sua carteira de trabalho: '))
# if cadastro['ctps'] != 0:
#     cadastro['contratacao'] = int(input('Digite o ano de sua contratacao: '))
#     cadastro['salário'] = float(input('Digite seu salario: '))
#     cadastro['aposentadoria'] = 0
#     cadastro['aposentadoria'] = (cadastro['contratacao'] - idade) + 35
# print('+='*30)
# for k, v in cadastro.items():
#     print(f'{k} tem o valor {v}')

#####################################Exercicio4###########################################
# jogador = dict()
# gol = []
# entrada = int(input('Digite o numero de partidas do jogador: '))
# jogador['nome'] = str(input('Digite o nome do jogador: '))
# jogador['soma'] = 0
# jogador['gol'] = gol
# for i in range(0, entrada):
#     gol.append(int(input(f'Quantos gols o {jogador["nome"]} fez na partida {i}: ')))
# for i in gol:
#     jogador['soma'] += i
# #     poderia usar a funcao soma
# for k, v in jogador.items():
#     print(f'{k} tem o valor {v}')
# print('=+'*30)
# print(f'O jogador {jogador["nome"]} jogou {len(jogador["gol"])} partidas')
# print('=+'*30)
# for i, g in enumerate(jogador['gol']):
#     print(f'=> Na partida {i}, fez {g} gols!')
# print(f'Foi um total de {jogador["soma"]} gols')
# segunda etapa
#####################################Exercicio5###########################################
# listagem = []
# dados = dict()
# count = 0
# mulheres = []
# media = 0
# velhos = []
# while True:
#     dados['nome'] = str(input('Digite seu nome: '))
#     count += 1
#     while True:
#         dados['sexo'] = str(input('Digite seu sexo [M/F]: ')).strip()[0].upper()
#         if dados["sexo"] != 'F' or dados["sexo"] != 'M':
#             break
#         print('Insira um caracter valido!!')
#     dados['idade'] = int(input('Digite sua idade: '))
#     media += (dados['idade'])/ count
#     listagem.append(dados.copy())
#     while True:
#         d = str(input('Deseja continuar[S/N]? ')).upper()
#         if d in 'SN':
#             break
#     if d == 'N':
#         break
# print(f'O numero de pessoas cadastradas foi de {count}')
# print(f'A media de idade entre os Cadastrados é {media:.2f}')
# print('+='*30)
# print(f'As mulheres cadastradas foram: ',end='')
# for i in listagem:
#     if i['sexo'] == 'F':
#         print(f'{i["nome"]} ', end='')
# print("")
# print('Alista de pessoas acima de media é de: ')
# for i in listagem:
#     if i['idade'] >= media:
#         print('  ')
#         for k, v in i.items():
#             print(f'{k}:{v};' , end='')
#         print("")
# print('Programa Finalizado!!!')
#####################################Exercicio6###########################################
# t = []
# jogador = dict()
# gol = []
# count = 0
# escolha = 0
# while True:
#     entrada = int(input('Digite o numero de partidas do jogador: '))
#     jogador['nome'] = str(input('Digite o nome do jogador: '))
#     gol.clear()
#     for i in range(0, entrada):
#         gol.append(int(input(f'Quantos gols o {jogador["nome"]} fez na partida {i+1}: ')))
#         count += 1
#         jogador['gol'] = gol[:]
#         jogador['soma'] = sum(gol)
#     t.append(jogador.copy())
#     while True:
#         d = str(input('Deseja continuar[S/N]?')).strip().upper()[0]
#         if d in 'SN':
#             break
#         print('Responda S/N !!')
#     if d == 'N':
#         for i, v in enumerate(t):
#             print(f'{i}    {v["nome"]}    {v["gol"]}    {v["soma"]}')
#         print(t)
#         break
# while True:
#     craque = int(input('Qual jogador que você deseja saber: '))
#     if craque == 999:
#         break
#     if craque >= len(t):
#         print('Numero nao existe tente de novo!!')
#     else:
#         print(f'Buscando jogador {t[craque]["nome"]}')
#     for k, v in enumerate(t[craque]["nome"]):
#         print(f'     => No jogo {k+1} ele fez {v} gols')