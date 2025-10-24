from funcoes import define_posicoes, preenche_frota, posicao_valida

tipos_navios = {
    "porta-aviões": {"quantidade": 1, "tamanho": 4},
    "navio-tanque": {"quantidade": 2, "tamanho": 3},
    "contratorpedeiro": {"quantidade": 3, "tamanho": 2},
    "submarino": {"quantidade": 4, "tamanho": 1}
}

frota = {}

for nome_navio, info in tipos_navios.items():
    quantidade = info["quantidade"]
    tamanho = info["tamanho"]
    for _ in range(quantidade):
        while True:
            print(f"Insira as informações referentes ao navio {nome_navio} que possui tamanho {tamanho}")
            linha = int(input())
            coluna = int(input())
            if tamanho > 1:
                orient = int(input())
                orientacao = "vertical" if orient == 1 else "horizontal"
            else:
                orientacao = "horizontal"
            if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                frota = preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho)
                break
            else:
                print("Esta posição não está válida!")

print(frota)