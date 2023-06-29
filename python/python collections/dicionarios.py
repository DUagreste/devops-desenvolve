aparicoes = {
    'João': 1,
    'cachorro': 2,
    'nome': 2,
    'vindo': 1
}

type(aparicoes)

aparicoes['João']

aparicoes.get('xpto', 0)

aparicoes['Carlos'] = 1

del aparicoes['Carlos']

'cachorro' in aparicoes

for i in aparicoes:
    print(i)

for i in aparicoes.keys():
    print(i)

for i in aparicoes.values():
    print(i)

for i in aparicoes.keys():
    print(i, aparicoes[i])

for chave, valor in aparicoes.items():
    print(chave, '=', valor)

# palavra = [f'palavra {}' for chave in aparicoes.keys()]