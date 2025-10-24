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

def posiciona_frota(frota):
    tabuleiro = [[0] * 10 for _ in range(10)]
    for nome, posicoes in frota.items():
        for posicao in posicoes:
            for p in posicao:
                linha = p[0]
                coluna = p[1]
                tabuleiro[linha][coluna] = 1
    return tabuleiro

def afundados(frota, tabuleiro):
    retorno = 0
    for nome, lista_navios in frota.items():
        for navio in lista_navios:
            afundado = True
            for linha, coluna in navio:
                if tabuleiro[linha][coluna] != 'X':
                    afundado = False
                    break
            if afundado:
                retorno += 1
    return retorno

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes_novas = define_posicoes(linha, coluna, orientacao, tamanho)
    
    for posicao in posicoes_novas:
        l, c = posicao
        if l < 0 or l > 9 or c < 0 or c > 9:
            return False
    
        posicoes_ocupadas = []
    for lista_navios in frota.values():
        for navio in lista_navios:
            for posicao in navio:
                posicoes_ocupadas.append(posicao)
    
    for posicao in posicoes_novas:
        if posicao in posicoes_ocupadas:
            return False  # Já ocupado
    
    return True