import random
playermatriz5 = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]
compmatriz5 = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]
print("Você vai jogar batalha naval!!! Legal sério.")

playerNav = 0
compNav = 0

#impedir que escolha o mesmo lugar
#Define posições dos navios do computador
for i in range(5):
    escolhaA = random.randint(0, 4)
    escolhaB = random.randint(0, 9)
    compmatriz5[escolhaA][escolhaB] = "X"
    compNav +=1

for i in compmatriz5:
    print(i)

#Define posições dos navios do jogador

#impedir que usurio digite a mesma linha e coluna
for i in range(5):
    linha = int(input(f"Escolha a {i + 1}° linha do seu navio: "))
    coluna = int(input(f"Escolha a {i + 1}° coluna do seu navio: "))
    coluna -= 1
    linha -= 1
    playermatriz5[linha][coluna] = "X"
    playerNav +=1

for i in playermatriz5:
    print(i)

while playerNav > 0 and compNav > 0:

    jogadorLinha = int(input("Escolha a linha que deseja atirar: "))
    jogadorColuna = int(input("Escolha a coluna que deseja atirar: "))
    jogadorColuna -= 1
    jogadorLinha -= 1

    if compmatriz5[jogadorLinha][jogadorColuna] == "X":
        print("Você derrubou um navio")
        #fazer implementaçao de navios restantes
        compNav -= 1
    else:
        print("você não acertou nenhum navio🤣")

    compLinha = random.randint(0, 4)
    compColuna = random.randint(0, 9)
    if playermatriz5[compLinha][compColuna] == "X":
        print("Derrubaram um navio seu!")
        playerNav -= 1
    else:
        print("Não derrubaram nenhum navio seu!")









