import sys

mapa = [["bigodudo",0,0, 0],
        ["capeta",0, 0,0],
        [0,0,0, 0],
        [0,0,0,0]]

def validarLinha(tabuleiro, linha, coluna, peca):
    count = 0 
    for i in range(len(tabuleiro)):
        if peca == "capeta":
            if coluna+i < len(tabuleiro)-1:
                if tabuleiro[linha][coluna + i] == "bigodudo":
                    count += 1
                if tabuleiro[linha][coluna + i] == "capeta":
                    break
            else:
                count += 1
                break   
        else:
            if coluna+i < len(tabuleiro)-1:
                if tabuleiro[linha][coluna + i] == "capeta":
                    count += 1
                    break
                if tabuleiro[linha][coluna + i] == "bigodudo":
                    break
            else:
                count += 1
                break
                
    if count == 1:
        for i in range(len(tabuleiro)):
            if peca == "capeta":
                if coluna-i > 0:
                    if tabuleiro[linha][coluna - i] == "bigodudo":
                        count += 1
                    if tabuleiro[linha][coluna - i] == "capeta":
                        break
                else:
                    count += 1
                    break
            else:
                if coluna-i > 0:
                    if tabuleiro[linha][coluna - i] == "capeta":
                        count += 1
                        break
                    if tabuleiro[linha][coluna - i] == "bigodudo":
                        break
                else:
                    count += 1
                    break

    if count == 2:
        return True
    else:
        return False
    
def validarColuna(tabuleiro, linha, coluna, peca):
    count = 0 
    for i in range(len(tabuleiro)):
        if peca == "capeta":
            if linha+i < len(tabuleiro):
                if tabuleiro[linha+i][coluna] == "bigodudo":
                    count += 1
                if tabuleiro[linha+i][coluna] == "capeta":
                    break
            else:
                count += 1
                break
                
        else:
            if linha+i < len(tabuleiro):
                if tabuleiro[linha+i][coluna] == "capeta":
                    count += 1
                    break
                if tabuleiro[linha+i][coluna] == "bigodudo":
                    break
            else:
                count += 1
                break
                
    if count == 1:
        for i in range(len(tabuleiro)):
            if peca == "capeta":
                if linha-i >= 0:
                    if tabuleiro[linha - i][coluna] == "bigodudo":
                        count += 1
                    if tabuleiro[linha - i][coluna] == "capeta":
                        break
                else:
                    count += 1
                    break
            else:
                if linha-i >= 0:
                    if tabuleiro[linha - i][coluna] == "capeta":
                        count += 1
                        break
                    if tabuleiro[linha - i][coluna] == "bigodudo":
                        break
                else:
                    count += 1
                    break

    if count == 2:
        return True
    else:
        return False

def validar(tabuleiro, linha, coluna, peca):
    return validarLinha(tabuleiro, linha, coluna, peca) and validarColuna(tabuleiro, linha, coluna, peca)

print(validar(mapa, 2, 0, "bigodudo"))
    
    
