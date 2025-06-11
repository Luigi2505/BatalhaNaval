from time import sleep
import random


def menucomp():
    print("\nTabuleiro Computador: \n")
    sleep(1)
    for j in tabuleiroComp:
        print(j)
    sleep(1)
    print(f"\nNavios restantes: {compNav} \n")
    print("---------------------------------")
    sleep(1)

def menuplayer():
    print("Tabuleiro Player: \n")
    sleep(1)
    for j in playermatriz:
        print(j)
    sleep(1)
    print(f"\nNavios restantes: {playerNav}")
    print("---------------------------------")
    sleep(1)

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


def ataque(direcao):
    while True:
        valor = int(input(f"\nEscolha uma {direcao} entre 1 e 10: "))
        if valor >= 1 and valor <= 10:
            return valor - 1
        else:
            print(f"{direcao} inválida! Digite um número entre 1 e 10.")


playermatriz = []
compmatriz = []
tabuleiroComp = []

def criarMatriz():
    matriz = []
    for linha in range(10):
        coluna = ["-"] * 10
        matriz.append(coluna)
    return matriz

playermatriz = criarMatriz()
compmatriz = criarMatriz()
tabuleiroComp = criarMatriz()

print("Você vai jogar batalha naval!!!")
player = input("Qual o seu nome?: ")


# Define posições dos navios do jogador
playerNav = 0
compNav = 0

# Lista com os tamanhos dos navios
tamanhos_navios = [5, 4, 3, 2, 1]

# Gera os navios do computador na matriz compmatriz5
for tamanho in tamanhos_navios:
    if colocar_navio_direcional(compmatriz, tamanho):
        compNav += tamanho

# Gera os navios do jogador aleatoriamente na matriz playermatriz
print("\nPosicionando seus navios aleatoriamente no tabuleiro 10x10")
sleep(1)
for tamanho in tamanhos_navios:
    if colocar_navio_direcional(playermatriz, tamanho):
        playerNav += tamanho
print("Seus navios foram posicionados!")
sleep(1)


# printa tabuleiros e navios restantes
menucomp()
menuplayer()

# Roda enquanto tiver o computador ou jogador possuir navios
while playerNav > 0 and compNav > 0:

    # Ataque do player
    playerLinha = ataque("linha")
    playerColuna = ataque("coluna")

    while tabuleiroComp[playerLinha][playerColuna] == "O" or tabuleiroComp[playerLinha][playerColuna] == "X":
        print("\nLinha e Coluna já escolhidas!")
        playerLinha = ataque("linha")
        playerColuna = ataque("coluna")

    print("---------------------------------")

    if compmatriz[playerLinha][playerColuna] == "1":
        print("\nVocê derrubou um navio!")
        sleep(1)
        compNav -= 1
        tabuleiroComp[playerLinha][playerColuna] = "X"

    else:
        print("\nVocê não acertou nenhum navio!")
        sleep(1)
        tabuleiroComp[playerLinha][playerColuna] = "O"

    menucomp()

    # Ataque do computador
    compLinha = random.randint(0, 9)
    compColuna = random.randint(0, 9)

    while playermatriz[compLinha][compColuna] == "O" or playermatriz[compLinha][compColuna] == "X":
        compLinha = random.randint(0, 9)
        compColuna = random.randint(0, 9)

    print(f"\nComputador atacou sua linha {compLinha + 1} e coluna {compColuna + 1}")
    sleep(1)
    if playermatriz[compLinha][compColuna] == "1":
        print("\nDerrubaram um navio seu!\n")
        sleep(1)
        playerNav -= 1
        playermatriz[compLinha][compColuna] = "X"
    else:
        print("\nNão derrubaram nenhum navio seu!\n")
        sleep(1)
        playermatriz[compLinha][compColuna] = "O"

    menuplayer()

# Printa vencedor e agradecimento
if playerNav == 0:
    print("Você perdeu! Vitória do Computador")
else:
    print(f"Você Ganhou! Vitória do {player}")

sleep(1)
print("Obrigado por jogar Batalha Naval \nFeito por \nEric Juan\nLuigi Bilyk\nGuilherme Albuquerque")