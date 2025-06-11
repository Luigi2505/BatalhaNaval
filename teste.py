def whileteste(matriz, linha, coluna):
    while matriz[linha][coluna] == "O" or matriz[linha][coluna] == "X":
        if jogador == 'player':
            print("\nLinha e Coluna já escolhidas!")
            playerLinha = ataque("linha")
            playerColuna = ataque("coluna")
        else:
            compLinha = random.randint(0, 9)
            compColuna = random.randint(0, 9)



while playermatriz[compLinha][compColuna] == "O" or playermatriz[compLinha][compColuna] == "X":
    compLinha = random.randint(0, 9)
    compColuna = random.randint(0, 9)

while tabuleiroComp[playerLinha][playerColuna] == "O" or tabuleiroComp[playerLinha][playerColuna] == "X":
        print("\nLinha e Coluna já escolhidas!")
        playerLinha = ataque("linha")
        playerColuna = ataque("coluna")
