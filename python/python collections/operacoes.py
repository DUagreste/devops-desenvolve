usuarios = {1, 5, 76, 34, 52, 13, 17}
len(usuarios)

usuarios.add(13)
usuarios.add(765)

usuarios = frozenset(usuarios)

meu_texto = 'Bem vindo meu nome é João eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro'
meu_texto_set = set(meu_texto.split(' '))

print(meu_texto_set)