from time import sleep
import random
from colorama import Fore, Style, init
init()

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
player = input("Qual o seu nome?: ")

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
    coluna = int(input(f"Escolha a {i}° coluna do seu navio: "))
    coluna -= 1
    linha -= 1
    # impede que o jogador escolha no mesmo lugar
    if playermatriz5[linha][coluna] != "1":
        playerNav +=1
    else:
        print("\nLinha e coluna já escolhida!\nEscolha outra!")
        i -= 1
    playermatriz5[linha][coluna] = "1"


#printa tabuleiros e navios restantes
menucomp()
menuplayer()


#Roda enquanto tiver o computador ou jogador possuir navios
while playerNav > 0 and compNav > 0:

    # escolha da linha e coluna do player
    jogadorLinha = int(input("\nEscolha a linha que deseja atirar: "))
    jogadorColuna = int(input("\nEscolha a coluna que deseja atirar: "))
    jogadorColuna -= 1
    jogadorLinha -= 1
    print("---------------------------------")

    if compmatriz5[jogadorLinha][jogadorColuna] == "1":
        print("\nVocê derrubou um navio!")
        sleep(1)
        compNav -= 1
        tabuleiroComp[jogadorLinha][jogadorColuna] = "X"

    else:
        print("\nVocê não acertou nenhum navio!")
        sleep(1)
        tabuleiroComp[jogadorLinha][jogadorColuna] = "O"

    menucomp()


#escolha da linha e coluna do computador
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










