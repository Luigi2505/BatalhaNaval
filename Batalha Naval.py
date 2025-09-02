from time import sleep
import random

#Função para exibir o tabuleiro e navios restantes
def menu(jogador, matriz, navio):
    print(f"\nTabuleiro {jogador}: \n")
    sleep(1)
    for i in matriz:
        print(i)
    sleep(1)
    print(f"\nNavios restantes: {navio} \n")
    print("---------------------------------")
    sleep(1)

#funçao para atacar
def ataque(direcao):
    while True:
        valor = int(input(f"\nEscolha uma {direcao} entre 1 e 10: "))
        if 1 <= valor <= 10:
            return valor - 1
        else:
            print(f"{direcao} inválida! Digite um número entre 1 e 10.")

#processa o ataque atualizando as matrizes
def processar_ataque(linha, coluna, matriz, navio, jogador, tabuleiro):
    print("---------------------------------")
    if matriz[linha][coluna] == "1":
        print(f"\n{jogador} derrubou um navio!")
        sleep(1)
        navio -= 1
        tabuleiro[linha][coluna] = "X"
    else:
        print(f"\n{jogador} não acertou nenhum navio!")
        sleep(1)
        tabuleiro[linha][coluna] = "O"
    return navio

#função para criar matriz
playermatriz = []
compmatriz = []
tabuleiroComp = []
def criarmatriz():
    matriz = []
    for linha in range(10):
        coluna = ["-"] * 10
        matriz.append(coluna)
    return matriz

playermatriz = criarmatriz()
compmatriz = criarmatriz()
tabuleiroComp = criarmatriz()

#funçao para checar se a coordenada ja foi atacada antes
def validar_ataque(matriz, linha, coluna, jogador):
    while matriz[linha][coluna] == "O" or matriz[linha][coluna] == "X":
        if jogador == "Player":
            print("\nLinha e Coluna já escolhidas!")
            linha = ataque("linha")
            coluna = ataque("coluna")
        elif jogador == "Computador":
            linha = random.randint(0, 9)
            coluna = random.randint(0, 9)
    return linha, coluna

#Funçao para posicionar os navios nos tabuleiros
def colocar_navio_direcional(tabuleiro, tamanho_navio):
    max_linhas = 10
    max_colunas = 10
    direcoes = ["cima", "baixo", "esquerda", "direita"]

    while True:
        linha = random.randint(0, max_linhas - 1)
        coluna = random.randint(0, max_colunas - 1)
        direcao = random.choice(direcoes)
        posicoes = []
        valido = True

        for i in range(tamanho_navio):
            if direcao == "cima":
                nova_linha, nova_coluna = linha - i, coluna
            elif direcao == "baixo":
                nova_linha, nova_coluna = linha + i, coluna
            elif direcao == "esquerda":
                nova_linha, nova_coluna = linha, coluna - i
            else:  # 'direita'
                nova_linha, nova_coluna = linha, coluna + i
            
            #verifica se esta dentro da matriz
            if 0 <= nova_linha < max_linhas and 0 <= nova_coluna < max_colunas:
                #verifica se não existe um barco nessa posição
                if tabuleiro[nova_linha][nova_coluna] == "-":
                    posicoes.append((nova_linha, nova_coluna))
                else:
                    valido = False
                    break
            else:
                valido = False
                break

        if valido:
            for l, c in posicoes:
                tabuleiro[l][c] = "1"
            return True

#Inicio do jogo
print("Você vai jogar batalha naval!!!")
player = input("Qual o seu nome?: ")

# Inicia contador de navios
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
menu("Computador", tabuleiroComp, compNav)
menu("Player", playermatriz, playerNav)

# Roda enquanto tiver o computador ou jogador possuir navios
while playerNav > 0 and compNav > 0:

    # Ataque do player
    playerLinha = ataque("linha")
    playerColuna = ataque("coluna")

    playerLinha, playerColuna = validar_ataque(tabuleiroComp, playerLinha, playerColuna, "Player")

    compNav = processar_ataque(playerLinha, playerColuna, compmatriz, compNav, "Você", tabuleiroComp)
    menu("Computador", tabuleiroComp, compNav)

    # Ataque do computador
    compLinha = random.randint(0, 9)
    compColuna = random.randint(0, 9)

    compLinha, compColuna = validar_ataque(playermatriz, compLinha, compColuna, "Computador")

    playerNav = processar_ataque(compLinha, compColuna, playermatriz, playerNav, "Computador", playermatriz)
    menu("Player", playermatriz, playerNav)

# Printa vencedor e agradecimento
if playerNav == 0:
    print("Você perdeu! Vitória do Computador")
else:
    print(f"Você Ganhou! Vitória do {player}")

sleep(1)
print("Obrigado por jogar Batalha Naval \nFeito por \nEric Juan\nLuigi Bilyk\nGuilherme Albuquerque")