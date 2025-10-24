def define_posicoes(linha, coluna, orientacao, tamanho):
    retorno = []
    if orientacao == "vertical":
        i = linha
        while i < linha + tamanho:
            posicao = [i, coluna]
            retorno.append(posicao)
            i += 1
    elif orientacao == "horizontal":
        j = coluna
        while j < coluna + tamanho:
            posicao = [linha, j]
            retorno.append(posicao)
            j += 1
    return retorno

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio in frota:
        frota[nome_navio].append(posicoes)
    else:
        frota[nome_navio] = [posicoes]
    return frota

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = '-'
    elif tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    return tabuleiro