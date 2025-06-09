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
    for j in tabuleiroPlayer:
        print(j)
    sleep(1)
    print(f"\nNavios restantes: {playerNav}")
    print("---------------------------------")
    sleep(1)

def atqPlayerLinha():
    while True:
        playerLinha = int(input("\nescolhaColunaa uma linha entre 1 e 5: "))
        if 1 <= playerLinha <= 5:
            return playerLinha - 1
        else:
            print("Linha inválida! escolhaColunaa entre 1 e 5.")

def atqPlayerColuna():
    while True:
        playerColuna = int(input("\nescolhaColunaa uma coluna entre 1 e 10: "))
        if 1 <= playerColuna <= 10:
            return playerColuna - 1
        else:
            print("Coluna inválida! escolhaColunaa entre 1 e 10.")



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


print("Você vai jogar batalha naval!!!")
player = input("Qual o seu nome?: ")

#inicia a quantidade de navios
playerNav = 0
compNav = 0


#Define posições dos navios do computador
while True:
    comparacao = 0
    tamanhoNav =  5 - compNav
    tamanhoCerto = 5 - compNav
    escolhaLinha = random.randint(0, 9)
    escolhaColuna = random.randint(0, 9)
    direcao = random.randint(0,3) #0 = horizontal direita, 1 = horizontal esquerta, 2 = vertical baixo, 3 vertigal cima
    
    if escolhaColuna + tamanhoNav <= 10 and direcao == 0 and compmatriz5[escolhaLinha][escolhaColuna] == "-": 
        for i in range(tamanhoNav):
            if compmatriz5[escolhaLinha][escolhaColuna] == "-":
                compmatriz5[escolhaLinha][escolhaColuna] = "1"
                escolhaColuna = escolhaColuna + 1
                tamanhoNav -= 1 
                comparacao += 1
            elif compmatriz5[escolhaLinha][escolhaColuna] == "1":
                escolhaColuna = escolhaColuna - 1
                compmatriz5[escolhaLinha][escolhaColuna] = "-"
                tamanhoNav -= 1 
                comparacao = 0
        if comparacao == tamanhoCerto: 
            compNav += 1
    if escolhaColuna - tamanhoNav >= 0 and direcao == 1 and compmatriz5[escolhaLinha][escolhaColuna] == "-":
        for i in range(tamanhoNav):
            if compmatriz5[escolhaLinha][escolhaColuna] == "-":
                compmatriz5[escolhaLinha][escolhaColuna] = "1"
                escolhaColuna = escolhaColuna - 1
                tamanhoNav -= 1 
                comparacao += 1
            elif compmatriz5[escolhaLinha][escolhaColuna] == "1":
                escolhaColuna = escolhaColuna + 1
                compmatriz5[escolhaLinha][escolhaColuna] = "-"
                tamanhoNav -= 1
                comparacao = 0 
        if comparacao == tamanhoCerto: 
            compNav += 1
    if escolhaLinha + tamanhoNav <= 10 and direcao == 2 and compmatriz5[escolhaLinha][escolhaColuna] == "-": 
        for i in range(tamanhoNav):
            if compmatriz5[escolhaLinha][escolhaColuna] == "-":
                compmatriz5[escolhaLinha][escolhaColuna] = "1"
                escolhaLinha = escolhaLinha + 1
                tamanhoNav -= 1 
                comparacao += 1
            elif compmatriz5[escolhaLinha][escolhaColuna] == "1":
                escolhaLinha = escolhaLinha - 1
                compmatriz5[escolhaLinha][escolhaColuna] = "-"
                tamanhoNav -= 1 
                comparacao = 0
        if comparacao == tamanhoCerto: 
            compNav += 1
    if escolhaLinha - tamanhoNav >= 0 and direcao == 3 and compmatriz5[escolhaLinha][escolhaColuna] == "-":            
        for i in range(tamanhoNav):
            if compmatriz5[escolhaLinha][escolhaColuna] == "-":
                compmatriz5[escolhaLinha][escolhaColuna] = "1"
                escolhaLinha = escolhaLinha - 1
                tamanhoNav -= 1 
                comparacao += 1
            elif compmatriz5[escolhaLinha][escolhaColuna] == "1":
                escolhaLinha = escolhaLinha + 1
                compmatriz5[escolhaLinha][escolhaColuna] = "-"
                tamanhoNav -= 1 
                comparacao = 0
        if comparacao == tamanhoCerto: 
            compNav += 1
    #impede que o computador escolhaColunaa no mesmo lugar
    if compNav == 5:
        break
        
#Define posições dos navios do jogador
i = 0
while playerNav < 10:
    i += 1
    linha = int(input(f"escolhaColunaa a {i}° linha do seu navio: "))
    while linha > 10:
        print("escolhaColunaa uma linha menor ou igual a 10!")
        linha = int(input(f"escolhaColunaa a {i}° linha do seu navio: "))

    coluna = int(input(f"escolhaColunaa a {i}° coluna do seu navio: "))
    while coluna > 10:
        print("escolhaColunaa uma coluna menor ou igual a 10!")
        coluna = int(input(f"escolhaColunaa a {i}° coluna do seu navio: "))

    if linha <=10:
        linha -= 1
    if coluna <=10:
        coluna -= 1

    # impede que o jogador escolhaColunaa no mesmo lugar
    if playermatriz5[linha][coluna] != "1":
        playerNav +=1
    else:
        print("\nLinha e coluna já escolhaColunaida!\nescolhaColunaa outra!")
        i -= 1
    playermatriz5[linha][coluna] = "1"


#printa tabuleiros e navios restantes
menucomp()
menuplayer()


#Roda enquanto tiver o computador ou jogador possuir navios
while playerNav > 0 and compNav > 0:

    # Ataque do player
    playerLinha = atqPlayerLinha()
    playerColuna = atqPlayerColuna()

    while tabuleiroComp[playerLinha][playerColuna] == "O" or tabuleiroComp[playerLinha][playerColuna] == "X":
        print("\nLinha e Coluna já escolhaColunaidas!")
        playerLinha = atqPlayerLinha()
        playerColuna = atqPlayerColuna()


    print("---------------------------------")

    if compmatriz5[playerLinha][playerColuna] == "1":
        print("\nVocê derrubou um navio!")
        sleep(1)
        compNav -= 1
        tabuleiroComp[playerLinha][playerColuna] = "X"

    else:
        print("\nVocê não acertou nenhum navio!")
        sleep(1)
        tabuleiroComp[playerLinha][playerColuna] = "O"

    menucomp()


#Ataque do computador
    compLinha = random.randint(0, 4)
    compColuna = random.randint(0, 9)

    while tabuleiroPlayer[compLinha][compColuna] == "O" or tabuleiroPlayer[compLinha][compColuna] == "X":
        compLinha = random.randint(0, 4)
        compColuna = random.randint(0, 9)


    print(f"\nComputador atacou sua linha {compLinha + 1} e coluna {compColuna + 1}")
    sleep(1)
    if playermatriz5[compLinha][compColuna] == "1":
        print("\nDerrubaram um navio seu!\n")
        sleep(1)
        playerNav -= 1
        tabuleiroPlayer[compLinha][compColuna] = "X"
    else:
        print("\nNão derrubaram nenhum navio seu!\n")
        sleep(1)
        tabuleiroPlayer[compLinha][compColuna] = "O"

    menuplayer()

#Printa vencedor e agradecimento
if playerNav == 0:
    print("Você perdeu! Vitória do Computador")
else:
    print(f"Você Ganhou! Vitória do {player}")

sleep(1)
print("Obrigado por jogar Batalha Naval \nFeito por \nEric Juan\nLuigi Bilyk\nGuilherme Albuquerque")
