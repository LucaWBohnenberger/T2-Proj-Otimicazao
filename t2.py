import sys
import copy

mapa = [[0, 0, 0, 0], 
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]


def validarLinha(tabuleiro, linha, coluna, peca):
    count = 0
    for i in range(len(tabuleiro)):
        if peca == "c":
            if coluna + i < len(tabuleiro) - 1:
                if tabuleiro[linha][coluna + i] == "b":
                    count += 1
                    break
                if tabuleiro[linha][coluna + i] == "c":
                    return False, 0
        else:
            if coluna + i < len(tabuleiro) - 1:
                if tabuleiro[linha][coluna + i] == "c":
                    count += 1
                    break
                if tabuleiro[linha][coluna + i] == "b":
                    return False, 0

    for i in range(len(tabuleiro)):
        if peca == "c":
            if coluna - i >= 0:
                if tabuleiro[linha][coluna - i] == "b":
                    count += 1
                    break
                if tabuleiro[linha][coluna - i] == "c":
                    return False, 0
        else:
            if coluna - i >= 0:
                if tabuleiro[linha][coluna - i] == "c":
                    count += 1
                    break
                if tabuleiro[linha][coluna - i] == "b":
                    return False, 0
    return True, count
            

def validarColuna(tabuleiro, linha, coluna, peca):
    count = 0
    for i in range(len(tabuleiro)):
        if peca == "c":
            if linha + i < len(tabuleiro):
                if tabuleiro[linha + i][coluna] == "b":
                    count += 1
                    break
                if tabuleiro[linha + i][coluna] == "c":
                    return False, 0

        else:
            if linha + i < len(tabuleiro):
                if tabuleiro[linha + i][coluna] == "c":
                    count += 1
                    break
                if tabuleiro[linha + i][coluna] == "b":
                    return False, 0

    for i in range(len(tabuleiro)):
        if peca == "c":
            if linha - i >= 0:
                if tabuleiro[linha - i][coluna] == "b":
                    count += 1
                    break
                if tabuleiro[linha - i][coluna] == "c":
                    return False, 0
        else:
            if linha - i >= 0:
                if tabuleiro[linha - i][coluna] == "c":
                    count += 1
                    break
                if tabuleiro[linha - i][coluna] == "b":
                    return False, 0

    return True, count



def validarDiagonal(tabuleiro, linha, coluna, peca):
  
    for i in range(len(tabuleiro)):
        count = 0
        if peca == "c":
            if linha + i < len(tabuleiro):
                # Diagonal -45 graus
                if coluna + i < len(tabuleiro):
                    if tabuleiro[linha + i][coluna + i] == "b":
                        count += 1
                        break
                    if tabuleiro[linha + i][coluna + i] == "c":
                        return False, 0
                    
                # diagonal 45 graus
                if coluna - i >= 0:
                    if tabuleiro[linha + i][coluna - i] == "b":
                        count += 1
                        break
                    if tabuleiro[linha + i][coluna - i] == "c":
                        return False, 0

        else:
            if linha + i < len(tabuleiro):
                # Diagonal -45 graus
                if coluna + i < len(tabuleiro):
                    if tabuleiro[linha + i][coluna + i] == "c":
                        count += 1
                        break
                    if tabuleiro[linha + i][coluna + i] == "b":
                        return False, 0
                    
                # diagonal 45 graus
                if coluna - i >= 0:
                    if tabuleiro[linha + i][coluna - i] == "c":
                        count += 1
                        break
                    if tabuleiro[linha + i][coluna - i] == "b":
                        return False, 0

    for i in range(len(tabuleiro)):
        if peca == "c":
            if linha - i >= 0:
                if coluna + i < len(tabuleiro):
                    if tabuleiro[linha - i][coluna+i] == "b":
                        count += 1
                        break
                    if tabuleiro[linha - i][coluna+i] == "c":
                        return False, 0
                if coluna - i >= 0:
                    if tabuleiro[linha - i][coluna-i] == "b":
                        count += 1
                        break
                    if tabuleiro[linha - i][coluna-i] == "c":
                        return False, 0
        else:
            if linha - i >= 0:
                if coluna + i < len(tabuleiro):
                    if tabuleiro[linha - i][coluna+i] == "c":
                        count += 1
                        break
                    if tabuleiro[linha - i][coluna+i] == "b":
                        return False, 0
                if coluna - i >= 0:
                    if tabuleiro[linha - i][coluna-i] == "c":
                        count += 1
                        break
                    if tabuleiro[linha - i][coluna-i] == "b":
                        return False, 0

    return True, count

def validar(tabuleiro, linha, coluna, peca):
    val, count = validarLinha(tabuleiro, linha, coluna, peca)
    val2, count2 = validarColuna(tabuleiro, linha, coluna, peca)
    val3, count3 = validarDiagonal(tabuleiro, linha, coluna, peca)
    if val and val2 and val3:
        return True, count+count2+count3
    else:
        return False, 0
    
def validar_tabuleiro(tabuleiro):
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro)):
            peca = tabuleiro[i][j]
            if peca in ["c", "b"]:
                val, count = validar(tabuleiro, i, j, peca)
                if val and count < 2:
                    return False
    return True

def resolver(tabuleiro, linha, coluna, bigodudos, capetas, total):
    if bigodudos == 0 and capetas == 0:
        if validar_tabuleiro(tabuleiro):
            total[0] += 1
            # for i in range(len(tabuleiro)):
            #     print(tabuleiro[i])
            # print()
            return
    
    if linha == len(tabuleiro) and coluna == len(tabuleiro):
        return

    if bigodudos > 0:
        if validar(tabuleiro, linha, coluna, "b")[0]:
            tab = copy.deepcopy(tabuleiro)
            tab[linha][coluna] = "b"

            if linha < len(tabuleiro)-1:
                resolver(tab, linha+1, coluna, bigodudos-1, capetas, total)
            elif coluna < len(tabuleiro)-1:
                resolver(tab, 0, coluna+1, bigodudos-1, capetas, total)
                resolver(tabuleiro, 0, coluna+1, bigodudos, capetas, total)
            elif bigodudos == 0 and capetas == 0:
                if validar_tabuleiro(tabuleiro):
                    total[0] += 1
                    # for i in range(len(tabuleiro)):
                    #     print(tabuleiro[i])
                    # print()
                    return
    if linha < len(tabuleiro)-1:
        resolver(tabuleiro, linha+1, coluna, bigodudos, capetas, total)
    elif coluna < len(tabuleiro)-1:
        resolver(tabuleiro, 0, coluna+1, bigodudos, capetas, total)

    if capetas > 0:
        if validar(tabuleiro, linha, coluna, "c")[0]:
            tab = copy.deepcopy(tabuleiro)
            tab[linha][coluna] = "c"
            if linha < len(tabuleiro)-1:
                resolver(tab, linha+1, coluna, bigodudos, capetas-1, total)
            elif coluna < len(tabuleiro)-1:
                resolver(tab, 0, coluna+1, bigodudos, capetas-1, total)
            elif bigodudos == 0 and capetas == 0:
                if validar_tabuleiro(tabuleiro):
                    total[0] += 1
                    #for i in range(len(tabuleiro)):
                    #   print(tabuleiro[i])
                    # print()
                    return
    
valor = [0]
tamanho = int(sys.argv[1])
bigodudos = int(sys.argv[2])
capetas = int(sys.argv[3])

tabuleiro = [[0]*tamanho for i in range(tamanho)]

resolver(tabuleiro, 0, 0, bigodudos, capetas, valor)
print(valor)
