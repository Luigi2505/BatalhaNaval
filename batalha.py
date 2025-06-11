from time import sleep
import random

def menucomp():
    print("\nTabuleiro Computador: \n")
    sleep(1)
    for j in tabuleiroComp:
        print(j)
    sleep(1)
    print(f"\nSegmentos de navios restantes do Computador: {compNav} \n")
    print("---------------------------------")
    sleep(1)

def menuplayer():
    # Comportamento original: Mostra o tabuleiro de ataques recebidos.
    print("Tabuleiro Player: \n")
    sleep(1)
    for j in playermatriz5:
        print(j)
    sleep(1)
    print(f"\nSeus segmentos de navios restantes: {playerNav}")
    print("---------------------------------")
    sleep(1)

def atqPlayerLinha():
    while True:
        try:
            playerLinha = int(input("\nEscolha uma linha para atacar (1 a 10): "))
            if 1 <= playerLinha <= 10:
                return playerLinha - 1
            else:
                print("Linha inválida! Escolha um número entre 1 e 10.")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")


def atqPlayerColuna():
    while True:
        try:
            playerColuna = int(input("Escolha uma coluna para atacar (1 a 10): "))
            if 1 <= playerColuna <= 10:
                return playerColuna - 1
            else:
                print("Coluna inválida! Escolha um número entre 1 e 10.")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")


def colocar_navio_direcional(tabuleiro, tamanho_navio):
    max_linhas = 10
    max_colunas = 10
    direcoes = ['cima', 'baixo', 'esquerda', 'direita']

    while True:
        linha = random.randint(0, max_linhas - 1)
        coluna = random.randint(0, max_colunas - 1)
        direcao = random.choice(direcoes)
        posicoes = []
        valido = True

        for i in range(tamanho_navio):
            if direcao == 'cima':
                nova_linha, nova_coluna = linha - i, coluna
            elif direcao == 'baixo':
                nova_linha, nova_coluna = linha + i, coluna
            elif direcao == 'esquerda':
                nova_linha, nova_coluna = linha, coluna - i
            else:  # 'direita'
                nova_linha, nova_coluna = linha, coluna + i

            if 0 <= nova_linha < max_linhas and 0 <= nova_coluna < max_colunas:
                if tabuleiro[nova_linha][nova_coluna] == '-':
                    posicoes.append((nova_linha, nova_coluna))
                else:
                    valido = False
                    break
            else:
                valido = False
                break

        if valido:
            for l, c in posicoes:
                tabuleiro[l][c] = '1'
            return True

# Suas matrizes originais, agora com 10 linhas e 10 colunas
playermatriz5 = [

    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']

]

compmatriz5 = [

    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']

]
tabuleiroPlayer = [

    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']

]

tabuleiroComp = [

    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']

]


print("Você vai jogar Batalha Naval 10x10!!!")
player = input("Qual o seu nome?: ")

# Inicia a quantidade de segmentos de navios
playerNav = 0
compNav = 0

# Lista com os tamanhos dos navios
tamanhos_navios = [5, 4, 3, 2, 1]

# Gera os navios do computador na matriz compmatriz5
for tamanho in tamanhos_navios:
    if colocar_navio_direcional(compmatriz5, tamanho):
        compNav += tamanho

# Gera os navios do jogador aleatoriamente na matriz playermatriz5
print("\nPosicionando seus navios aleatoriamente no tabuleiro 10x10...")
sleep(1)
for tamanho in tamanhos_navios:
    if colocar_navio_direcional(playermatriz5, tamanho):
        playerNav += tamanho
print("Seus navios foram posicionados!")
sleep(1)
for j in playermatriz5:
        print(j)
# Mostra os tabuleiros iniciais
menucomp()
menuplayer()

# Loop principal do jogo
while playerNav > 0 and compNav > 0:

    # Ataque do jogador
    print("\nSua vez de atacar!")
    playerLinha = atqPlayerLinha()
    playerColuna = atqPlayerColuna()

    while tabuleiroComp[playerLinha][playerColuna] in ("O", "X"):
        print("\nVocê já atirou aí! Escolha outra coordenada.")
        playerLinha = atqPlayerLinha()
        playerColuna = atqPlayerColuna()

    print("---------------------------------")

    if compmatriz5[playerLinha][playerColuna] == "1":
        print("\nFOGO! Você acertou um navio inimigo!")
        sleep(1)
        compNav -= 1
        tabuleiroComp[playerLinha][playerColuna] = "X"
    else:
        print("\nÁGUA! Você errou o tiro.")
        sleep(1)
        tabuleiroComp[playerLinha][playerColuna] = "O"

    if compNav == 0:
        break

    menucomp()

    # Ataque do computador
    print("\nVez do computador atacar...")
    sleep(1)
    compLinha = random.randint(0, 9)
    compColuna = random.randint(0, 9)

    while tabuleiroPlayer[compLinha][compColuna] in ("O", "X"):
        compLinha = random.randint(0, 9)
        compColuna = random.randint(0, 9)

    print(f"\nComputador atacou a linha {compLinha + 1} e coluna {compColuna + 1}")
    sleep(1)
    
    # Lógica original: Verifica o acerto em 'playermatriz5', mas só atualiza 'tabuleiroPlayer'
    if playermatriz5[compLinha][compColuna] == "1":
        print("\nCUIDADO! Atingiram um de seus navios!\n")
        sleep(1)
        playerNav -= 1
        tabuleiroPlayer[compLinha][compColuna] = "X"
    else:
        print("\nUfa! O computador errou o tiro!\n")
        sleep(1)
        tabuleiroPlayer[compLinha][compColuna] = "O"

    menuplayer() # Chama a função que agora mostra o 'tabuleiroPlayer'


# Resultado final
print("---------------------------------")
if playerNav <= 0:
    print("\nFim de jogo! Você perdeu! O Computador venceu.")
else:
    print(f"\nFim de jogo! Parabéns, {player}! Você venceu!")

sleep(1)
print("\nObrigado por jogar Batalha Naval!")
print("Feito por: Eric Juan, Luigi Bilyk, Guilherme Albuquerque")