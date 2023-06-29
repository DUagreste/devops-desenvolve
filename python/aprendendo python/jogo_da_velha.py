# Módulos
import random
import os     


# Função geral do jogo
def jogar():
    # Mensagem de início
    print(33*"-")
    print("")
    print(27*"*")
    print("****** JOGO DA VELHA ******")
    print(27*"*")

    # Obtem o símbolo do jogador
    print("\nEscolha o seu símbolo:")
    print("\n1 - X")
    print("2 - O")

    while True:
        escolha = input("Digite 1 ou 2 para escolher o seu símbolo: ")
        if escolha == "1":
            jogador = "X"
            computador = "O"
            break
        elif escolha == "2":
            jogador = "O"
            computador = "X"
            break
        else:
            print("Escolha inválida. Digite 1 ou 2 para escolher o seu símbolo.\n")

    # Instruções para o jogo
    print("-"*27)
    print("Instruções:")
    print("Funciona como um jogo da velha convencional.")
    print("Vence quem completar primeiro uma coluna, uma linha ou uma diagonal.")
    print("Digite o número correspondente à posição onde deseja jogar.")
    print("-"*27)

    # Começo o jogo
    print(f"\nVocê jogará como '{jogador}'. O computador jogará como '{computador}'.\n")
    tabuleiro = [" "] * 10
    jogadores = {1: jogador, 2: computador}
    mostrar_tabuleiro(tabuleiro)

    # Loop do jogo
    while True:
        # Vez do Jogador
        while True:
            posicao = input("Digite a posição para jogar (1-9): ")
            if posicao.isdigit() and int(posicao) in range(1, 10):
                posicao = int(posicao)
                if realizar_jogada(tabuleiro, jogadores[1], posicao):
                    break
                else:
                    print("Posição já ocupada. Tente novamente.\n")
            else:
                print("Posição inválida. Digite um número de 1 a 9 para jogar.\n")
        print("")
        mostrar_tabuleiro(tabuleiro)

        if checar_vitoria(tabuleiro, jogadores[1]) or checar_empate(tabuleiro):
            jogar_de_novo = jogar_novamente()
            if not jogar_de_novo:
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                tabuleiro = [" "] * 10
                print("="*30)
                print("")
                mostrar_tabuleiro(tabuleiro)
                continue

        # Vez do computador
        posicoes_vazias = [i for i in range(1, 10) if tabuleiro[i] == " "]
        if posicoes_vazias:
            posicao = random.choice(posicoes_vazias)

        realizar_jogada(tabuleiro, jogadores[2], posicao)
        print(f"Jogada automática do '{computador}': {posicao}\n")

        mostrar_tabuleiro(tabuleiro)

        if checar_vitoria(tabuleiro, jogadores[2]) or checar_empate(tabuleiro):
            jogar_de_novo = jogar_novamente()
            if not jogar_de_novo:
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                tabuleiro = [" "] * 10
                print("="*30)
                print("")
                mostrar_tabuleiro(tabuleiro)
                continue

            
# Exibe o tabuleiro no estado atual
def mostrar_tabuleiro(tabuleiro):
    print(f" {tabuleiro[1]} | {tabuleiro[2]} | {tabuleiro[3]} ")
    print("---|---|---")
    print(f" {tabuleiro[4]} | {tabuleiro[5]} | {tabuleiro[6]} ")
    print("---|---|---")
    print(f" {tabuleiro[7]} | {tabuleiro[8]} | {tabuleiro[9]} ")
    print()


# Permite que o jogador faça uma jogada
def realizar_jogada(tabuleiro, jogador, posicao):
    if tabuleiro[posicao] == " ":
        tabuleiro[posicao] = jogador
        return True
    else:
        return False


# Verifica se um dos jogadores venceu
def checar_vitoria(tabuleiro, jogador):
    vitorias = [[1, 2, 3], [4, 5, 6], [7, 8, 9], # linhas
                [1, 4, 7], [2, 5, 8], [3, 6, 9], # colunas
                [1, 5, 9], [3, 5, 7]]            # diagonais   

    for i, j, k in vitorias:
        if tabuleiro[i] == tabuleiro[j] == tabuleiro[k] == jogador:
            print(f'O jogador {jogador} ganhou o jogo! :)')
            return True
    return False


# Verifica se houve empate
def checar_empate(tabuleiro):
    for i in range(1, 10):
        if tabuleiro[i] == " ":
            return False
    print("O jogo empatou!")
    return True


# Permite que o jogador escolha X ou O como seu símbolo
def obter_simbolo_jogador():
    while True:
        simbolo = input("\nEscolha X ou O: ")
        if simbolo.upper() == "X":
            return "X", "O"
        elif simbolo.upper() == "O":
            return "O", "X"
        else:
            print("Opção inválida. Tente novamente.")


# Para o computador efetuar suas jogadas automaticamente
def jogada_automatica(tabuleiro, jogador):
    posicoes_vazias = [i for i in range(1, 10) if tabuleiro[i] == " "]
    if posicoes_vazias:
        return random.choice(posicoes_vazias)
    else:
        return None


# Permite que o jogador escolha se deseja jogar novamente
def jogar_novamente():
    while True:
        jogar_denovo = input("\nDeseja jogar novamente (s/n)? ").lower()
        print("")
        if jogar_denovo == "s":
            return True
        elif jogar_denovo == "n":
            print("-"*30)
            print("Obrigado por jogar. Até a próxima!")
            print("-"*30)
            return False
        else:
            print("\nEntrada inválida. Digite 's' para SIM e 'n' para NÃO.")

            

if (__name__ == "__main__"):
    jogar()