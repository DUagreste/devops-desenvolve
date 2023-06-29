import forca 
import advinhacao
import blackjack
import jogo_da_velha

def escolher_jogo():
    print(35*"*")
    print("*** BEM VINDO AO SALÃO DE JOGOS ***")
    print(35*"-")
    print("")
    print("1 -> Advinhação")
    print("2 -> Forca")
    print("3 -> BlackJack")
    print("4 -> Jogo da Velha")
    print("")
    jogo = int(input("Digite o jogo desejado: "))

    if (jogo == 1):
        advinhacao.jogar()
    elif (jogo == 2):
        forca.jogar()
    elif (jogo == 3):
        blackjack.jogar()
    elif (jogo == 4):
        jogo_da_velha.jogar()


if (__name__ == "__main__"):
    escolher_jogo()