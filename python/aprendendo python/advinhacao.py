from random import randint

def jogar():

    print(33*"-")
    print("")
    print(30*"*")
    print("***** JOGO DA ADVINHAÇÃO *****")

    codigo = randint(1,100)
    pontos = 500

    print(30*"-")
    print("***** Dificuldades *****")
    print("3 -> Difícil")
    print("2 -> Normal")
    print("1 -> Fácil")
    dificuldade = int(input("Digite o nível desejado: "))

    if (dificuldade == 1):
        numero_tentativas = 15
    elif (dificuldade == 2):
        numero_tentativas = 10
    elif (dificuldade == 3):
        numero_tentativas = 5
    else:
        print("***** Você não escolheu uma dificuldade válida *****")
        exit()

    for rodada in range(1, numero_tentativas + 1):
        print(35*"-")
        palpite_str = input("Digite o seu palpite (1~100): ")
        palpite = int(palpite_str)
        print("Você digitou {}.".format(palpite))

        if (palpite < 1 or palpite > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = palpite == codigo
        maior   = palpite > codigo
        menor   = palpite < codigo

        if (acertou):
            print("***** PARABÉNS, VOCê ACERTOU O CÓDIGO! *****")
            print("***** {} pontos *****".format(pontos))
            break
        else:
            numero_tentativas += 1
            pontos_perdidos = abs(codigo - palpite)
            pontos = pontos - pontos_perdidos
            if(maior):
                print("Você errou! Chute mais baixo!")
            elif(menor):
                print ("Você errou! Chute mais alto!")
    else:
        pontos = 0
        print(35*"*")
        print("Infelizmente, você fez 0 pontos!")
        print("O código correto era {}! Tente novamente!".format(codigo))

if(__name__ == "__main__"):
    jogar()