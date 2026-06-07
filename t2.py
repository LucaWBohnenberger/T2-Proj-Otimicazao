import sys

DIRECOES_TODAS = [
    (-1, 0), (1, 0), (0, -1), (0, 1), 
    (-1, -1), (-1, 1), (1, -1), (1, 1)
]

DIRECOES_PASSADO = [
    (0, -1),   # Esquerda
    (-1, 0),   # Cima
    (-1, -1),  # Diagonal Cima-Esquerda
    (-1, 1)    # Diagonal Cima-Direita
]

def pode_inserir(tabuleiro, linha, coluna, peca, tamanho):
    """Garante que a nova peça não veja um amigo nas lajotas já preenchidas."""
    for dl, dc in DIRECOES_PASSADO:
        l, c = linha + dl, coluna + dc
        while 0 <= l < tamanho and 0 <= c < tamanho:
            peca_encontrada = tabuleiro[l][c]
            if peca_encontrada == peca:
                return False  
            elif peca_encontrada != 0:
                break  
            l += dl
            c += dc
    return True

def validar_tabuleiro_final(tabuleiro, tamanho):
    for linha in range(tamanho):
        for coluna in range(tamanho):
            peca = tabuleiro[linha][coluna]
            if peca != 0:
                inimigo = "c" if peca == "b" else "b"
                count_inimigos = 0
                
                for dl, dc in DIRECOES_TODAS:
                    l, c = linha + dl, coluna + dc
                    while 0 <= l < tamanho and 0 <= c < tamanho:
                        peca_encontrada = tabuleiro[l][c]
                        if peca_encontrada == peca:
                            return False 
                        elif peca_encontrada == inimigo:
                            count_inimigos += 1
                            break
                        l += dl
                        c += dc
                        
                if count_inimigos < 2:
                    return False
    return True

def resolver(tabuleiro, linha, coluna, b, c, tamanho, total):
    if b == 0 and c == 0:
        if validar_tabuleiro_final(tabuleiro, tamanho):
            total[0] += 1
        return
    
    celulas_restantes = (tamanho * tamanho) - (linha * tamanho + coluna)
    if b + c > celulas_restantes:
        return

    if linha == tamanho:
        return

    prox_coluna = coluna + 1
    prox_linha = linha
    if prox_coluna == tamanho:
        prox_coluna = 0
        prox_linha = linha + 1

    if b > 0 and pode_inserir(tabuleiro, linha, coluna, "b", tamanho):
        tabuleiro[linha][coluna] = "b"
        resolver(tabuleiro, prox_linha, prox_coluna, b - 1, c, tamanho, total)
        tabuleiro[linha][coluna] = 0  

    if c > 0 and pode_inserir(tabuleiro, linha, coluna, "c", tamanho):
        tabuleiro[linha][coluna] = "c"
        resolver(tabuleiro, prox_linha, prox_coluna, b, c - 1, tamanho, total)
        tabuleiro[linha][coluna] = 0  

    resolver(tabuleiro, prox_linha, prox_coluna, b, c, tamanho, total)

if __name__ == "__main__":
    if len(sys.argv) >= 4:
        tamanho = int(sys.argv[1])
        bigodudos = int(sys.argv[2])
        capetas = int(sys.argv[3])

        tabuleiro = [[0]*tamanho for _ in range(tamanho)]
        valor = [0]

        resolver(tabuleiro, 0, 0, bigodudos, capetas, tamanho, valor)
        print(valor[0])
    else:
        print("Uso: python salao.py <n> <b> <c>")