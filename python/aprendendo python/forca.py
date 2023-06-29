import requests
from lxml import html  


def jogar():

    palavra_secreta = carregar_palavra_secreta()
    letras_acertadas = inicia_letras_acertadas(palavra_secreta)

    mensagem_boas_vindas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0
    letras_erradas = []

    while (not enforcou and not acertou):
        palpite = pede_palpite()
        
        if (palpite in palavra_secreta):
            print("Você acertou! A letra {} está na palavra secreta.\n".format(palpite))
            mostra_palpite_certo(palpite, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros, palpite, letras_erradas)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        
        print(letras_acertadas)
        
    if (acertou):
        imprime_mensagem_vencedor(palavra_secreta)
    else:
        imprime_mensagem_perdedor(palavra_secreta)    


def carregar_palavra_secreta():
    url = "https://www.palabrasaleatorias.com/palavras-aleatorias.php?fs=1&fs2=1&Submit=Nova+palavra"
    resposta = requests.get(url)
    elemento = html.fromstring(resposta.content)
    palavra_secreta = elemento.xpath('//div[@style="font-size:3em; color:#6200C5;"]/text()')
    palavra_secreta = palavra_secreta[0].strip().upper()
    return palavra_secreta


def inicia_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]


def pede_palpite():
    palpite = input("\nDigite uma letra: ")
    print("-------------------------------------\n")
    palpite = palpite.strip().upper()
    return palpite


def mostra_palpite_certo(palpite, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (palpite == letra):
            letras_acertadas[index] = letra
        index += 1


def mensagem_boas_vindas(palavra_secreta):
    print(33*"-")
    print("")
    print("  _______     ")
    print(" |/      |    ***********************")
    print(" |            **** JOGO DA FORCA ****")
    print(" |            ***********************")
    print(" |            ")
    print(" |            ")
    print(" |            A palavra da forca tem {} letras.".format(len(palavra_secreta)))
    print("_|___         ")
    print("")


def imprime_mensagem_vencedor(palavra_secreta):
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    PARABÉNS!")
    print("     | (|:.     |) |    Você venceu e conseguiu escapar da forca!")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          A palavra era {}.".format(palavra_secreta))
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \     FIM DA LINHA!")
    print(" |   XXXX     XXXX   |    Você perdeu e foi inforcado!")
    print(" |   XXXX     XXXX   |    ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   |  I I I I I I  |       A palavra era {}.".format(palavra_secreta))
    print("    \_           _/        ")
    print("       \_______/           ")


def desenha_forca(erros, palpite, letras_erradas):
    letras_erradas.append(palpite)
    print("  _______     ")
    print(" |/      |    ")
    
    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |              Não tem a letra {} na forca!".format(palpite))
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |              Não tem a letra {} na forca!".format(palpite))
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      /|    ")
        print(" |              Não tem a letra {} na forca!".format(palpite))
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      /|\   ")
        print(" |              Não tem a letra {} na forca!".format(palpite))
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      /|\   ")
        print(" |       |      Não tem a letra {} na forca!".format(palpite))
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      /|\   ")
        print(" |       |      Não tem a letra {} na forca!".format(palpite))
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      /|\   ")
        print(" |       |      Não tem a letra {} na forca!".format(palpite))
        print(" |      / \   ")

    print(" |               Letras erradas: {}.".format(letras_erradas))
    print("_|___         ")
    print()


if (__name__ == "__main__"):
    jogar()
