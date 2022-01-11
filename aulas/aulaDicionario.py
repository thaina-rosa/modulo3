# pessoas = {'nome': 'Thaina', 'sexo': 'M', 'idadde': 22}
# print(pessoas)
# diferente de listas nao pode chamar por indice, voce chama pela chave ou pelo valor

# print(pessoas['nome'])

# tambem da para fazer assim no key ou no value a chamada deve ter aspas completas

# print(f'O nome da pessoa é{pessoas["nome"]}')

#apenas chaves
# print(pessoas.keys())

#chave e valor
# print(pessoas.items())

# com laco for com key
# for k in pessoas.keys():
#     print(k)

# com laco for para chave e valor
# mudanca de valor

# pessoas['nome'] = 'Leandro'
# adicionando itens ainda n existentes
# pessoas['peso'] = 96.5

# for k, v in pessoas.items():
#     print(f'{k} = {v}')

# deletar itens
# del pessoas['sexo']
################################################################
# brasil = []
# estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
# estado2 = {'uf': 'Sao Paulo', 'sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)
# print(estado1)
# print(estado2)
# # aqui esta pedindo pela posicao na lista e a posicao no dicionario
# print(brasil[1]['sigla'])

################################################################
# nao da para copiar usando o [:]
# estado = dict()
# brasil = list()
# for c in range(0,3):
#     estado['uf'] = str(input('Digite o nome do estado: '))
#     estado['sigla'] = str(input('Digite a sigla do estado: '))
#     brasil.append(estado.copy())
# # print(brasil)
# for e in brasil:
#     # print(e)
#     for k, v in e.items():
#         # print(f'O campo {k} tem valor {v}.')
#         print(v, end=' ')
#     print("")