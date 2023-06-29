# Importando módulos e definindo variáveis

import random

def jogar():

    global jogando
    jogando = True

    # Variáveis essenciais para as cartas com seus 4 naipes, e os números e letras com suas respectivas pontuação
    naipes = ('♥', '♦', '♣', '♠')
    pontuacao = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    valores = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
            '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}


    # CLASSES

    # Criando as cartas
    class Carta:  

        def __init__(self, naipe, pontos):
            self.naipe = naipe
            self.pontos = pontos

        def __str__(self):
            return self.pontos + self.naipe


    # Criando as mãos de cartas do Jogador e crupie
    class Mao:    

        def __init__(self):
            self.cartas = []
            self.valor = 0
            self.ace = 0    # Acompanha os Aces

        # Adiciona cartas as mãos do Jogador e crupie quando quiserem puxar
        def adiciona_carta(self, carta):   
            self.cartas.append(carta)
            self.valor += valores[carta.pontos]
            if carta.pontos == 'A':
                self.ace += 1

        # Método para o Ace
        def ajusta_ace(self):   
            while self.valor > 21 and self.ace:
                self.valor -= 10
                self.ace -= 1


    # Criando o baralho
    class Baralho:    

        def __init__(self):
            self.baralho = []

            for naipe in naipes:
                for pontos in pontuacao:
                    self.baralho.append(Carta(naipe, pontos))

        def __str__(self):
            baralho_comp = ''
            for carta in self.baralho:
                baralho_comp += '\n ' + carta.__str__()
            return 'O baralho tem: ' + baralho_comp

        # Embaralha as cartas
        def embaralhar(self):    
            random.shuffle(self.baralho)

        # Escolhe UMA carta do baralho
        def puxar(self):    
            uma_carta = self.baralho.pop()
            return uma_carta


    # Para fazer apostas
    class Apostas:    

        # Define o valor da carteira do jogador
        def __init__(self):
            self.total = 100
            self.aposta = 0

        def aposta_vitoria(self):
            self.total += self.aposta

        def aposta_perdedora(self):
            self.total -= self.aposta


    # FUNÇÕES
    def mensagem_inicial():
        print("")
        print(33*"-")
        print("")
        print(33*'*')
        print("   ♠ ♣ ♦ ♥  BLACKJACK  ♥ ♦ ♣ ♠")
        print(33*'*')
        print("")


    # Faz a aposta
    def faça_aposta(apostas):   

        while True:
            try:
                apostas.aposta = int(input(f'Quanto você irá apostar: R$'))
            except ValueError:
                print('Desculpe, por favor digite um valor válido: ')
            else:
                if apostas.aposta > apostas.total:
                    print('Você não tem dinheiro suficiente!')
                else:
                    break

    # Ações para o hit
    def acerto(baralho, mao):   
        mao.adiciona_carta(baralho.puxar())
        mao.ajusta_ace()


    # Utilizado para verificar se o jogador quer permanecer com a pontuação atual ou arriscar puxar
    def hit_ou_stand(baralho, mao):     
                                        
        global jogando

        while True:
            pergunta = input("\nHit ou Stand? Digite 'H' ou 'S': ")

            if pergunta[0].lower() == 'h':
                acerto(baralho, mao)
            elif pergunta[0].lower() == 's':
                print(30*'-')
                print("Jogador fica, crupie ainda está jogando.")
                jogando = False
            else:
                print("Desculpe, eu não entendi. Por favor, tente novamente!")
                continue
            break

    
    # Mostra a mão inicial do jogador e do crupiê (com uma escondida)
    # Também irá mostrar as cartas puxadas pelo jogador
    def mostrar_mao(jogador, crupie):
        print("\nMão do crupie: ")      
        print(" <carta escondida> ")
        print("", crupie.cartas[1])
        print("\nMão do jogador:", *jogador.cartas, sep='\n')


    # Mostra a mão final do jogo, mostrando a carta escondida do crupie
    def mostrar_mao_geral(jogador, crupie):     
        print("Mão do crupie: ", *crupie.cartas, sep='\n')
        print("Valor da mão = ", crupie.valor)
        print("\nMão do jogador:", *jogador.cartas, sep='\n')
        print("Valor da mão = ", jogador.valor)


    # Final do jogo
    def jogador_perde(jogador, crupie, apostas):
        print("\n**** Jogador explodiu! ****")
        apostas.aposta_perdedora()


    def jogador_vence(jogador, crupie, apostas):
        print("\n**** Vitória do jogador! ****")
        apostas.aposta_vitoria()


    def crupie_perde(jogador, crupie, apostas):
        print("\n**** Crupie explodiu! ****")
        apostas.aposta_vitoria()


    def crupie_vence(jogador, crupie, apostas):
        print("\n**** Vitória do crupie! ****")
        apostas.aposta_perdedora()


    def empate(jogador, crupie):
        print("\n**** Empate entre o Jogador e o Crupie!****")


    # O jogo

    while True:
        mensagem_inicial()
        
        # Embaralhando e distribuindo as cartas
        baralho = Baralho()
        baralho.embaralhar()

        mao_jogador = Mao()
        mao_jogador.adiciona_carta(baralho.puxar())
        mao_jogador.adiciona_carta(baralho.puxar())

        mao_crupie = Mao()
        mao_crupie.adiciona_carta(baralho.puxar())
        mao_crupie.adiciona_carta(baralho.puxar())

        # Definindo o valor da carteira do Jogador
        jogador_apostas = Apostas()

        # Pergunta a aposta
        faça_aposta(jogador_apostas)

        # Mostrar as cartas
        mostrar_mao(mao_jogador, mao_crupie)

        while jogando:

            hit_ou_stand(baralho, mao_jogador)
            mostrar_mao(mao_jogador, mao_crupie)

            if mao_jogador.valor > 21:
                print(30*'-')
                mostrar_mao_geral(mao_jogador, mao_crupie)
                jogador_perde(mao_jogador, mao_crupie, jogador_apostas)
                break

        if mao_jogador.valor <= 21:

            while mao_crupie.valor < 17 or mao_crupie.valor <= mao_jogador.valor:
                acerto(baralho, mao_crupie)

            print(30*'-')
            mostrar_mao_geral(mao_jogador, mao_crupie)

            if mao_crupie.valor > 21:
                crupie_perde(mao_jogador, mao_crupie, jogador_apostas)

            elif mao_crupie.valor > mao_jogador.valor:
                crupie_vence(mao_jogador, mao_crupie, jogador_apostas)

            elif mao_crupie.valor < mao_jogador.valor:
                jogador_vence(mao_jogador, mao_crupie, jogador_apostas)

            elif mao_jogador.valor > 21:
                jogador_perde(mao_jogador, mao_crupie, jogador_apostas)

            else:
                empate(mao_jogador, mao_crupie)

        print(f"\nSua carteira: R${jogador_apostas.total}")
        print("-"*33)
        print("-"*33)
        new_game = input("\nJogar novamente? Digite 's' ou 'n': ")
        if new_game[0].lower() == 's':
            jogando = True
            continue
        else:
            print(20*'-')
            print("Obrigado por jogar. Até a próxima!")
            print(20*'-')
            break

if (__name__ == "__main__"):
    jogar()