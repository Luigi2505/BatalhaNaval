from time import sleep
import random

#função do tabuleiro e navios restantes do computador
def menucomp():
    print("\nTabuleiro do Computador: \n")
    sleep(1)
    for j in tabuleiroComp:
        print(j)
    sleep(1)
    print(f"\nNavios restantes do Computador: {compNav} \n")
    print("---------------------------------")
    sleep(1)

#função do tabuleiro e navios restantes do jogador
def menuplayer():
    print("Tabuleiro do Player: \n")
    sleep(1)
    for j in tabuleiroPlayer:
        print(j)
    sleep(1)
    print(f"\nNavios restantes do Player: {playerNav}")
    print("---------------------------------")
    sleep(1)
#função de ataque do player para linha e coluna do computador
def atqPlayerLinha():
    while True:
        playerLinha = int(input("\nEscolha uma linha entre 1 e 5: "))
        if 1 <= playerLinha <= 5:
            return playerLinha - 1
        else:
            print("Linha inválida! Escolha entre 1 e 5.")

def atqPlayerColuna():
    while True:
        playerColuna = int(input("\nEscolha uma coluna entre 1 e 10: "))
        if 1 <= playerColuna <= 10:
            return playerColuna - 1
        else:
            print("Coluna inválida! Escolha entre 1 e 10.")


#matrizes dos tabuleiros
playermatriz5 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
compmatriz5 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

tabuleiroPlayer = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
tabuleiroComp = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


print("Você vai jogar batalha naval!!!")
player = input("Escolha um Nome: ")

#inicia a quantidade de navios
playerNav = 0
compNav = 0


#Define posições dos navios do computador
while compNav < 5:
    escolhaA = random.randint(0, 4)
    escolhaB = random.randint(0, 9)
    #impede que o computador escolha no mesmo lugar
    if compmatriz5[escolhaA][escolhaB] != "1":
        compNav +=1
    compmatriz5[escolhaA][escolhaB] = "1"

#Define posições dos navios do jogador
i = 0
while playerNav < 5:
    i += 1
    linha = int(input(f"Escolha a {i}° linha do seu navio: "))
    while linha > 5:
        print("Escolha uma linha menor ou igual a 5!")
        linha = int(input(f"Escolha a {i}° linha do seu navio: "))

    coluna = int(input(f"Escolha a {i}° coluna do seu navio: "))
    while coluna > 10:
        print("Escolha uma coluna menor ou igual a 10!")
        coluna = int(input(f"Escolha a {i}° coluna do seu navio: "))

    if linha <=5:
        linha -= 1
    if coluna <=10:
        coluna -= 1

    # impede que o jogador escolha a mesma linha e coluna
    if playermatriz5[linha][coluna] != "1":
        playerNav +=1
    else:
        print("\nLinha e coluna já escolhida!\nEscolha outra!")
        i -= 1
    playermatriz5[linha][coluna] = "1"


#printa tabuleiros e navios restantes
menucomp()
menuplayer()


#loop para o codigo ser lido enquanto tiver navios do computador ou do player em jogo
while playerNav > 0 and compNav > 0:

    # Ataque do player
    playerLinha = atqPlayerLinha()
    playerColuna = atqPlayerColuna()
#impedindo o jogador de atacar o mesmo lugar
    while tabuleiroComp[playerLinha][playerColuna] == "O" or tabuleiroComp[playerLinha][playerColuna] == "X":
        print("\nLinha e Coluna já escolhidas!")
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