def criar_blocos(nivel):
    blocos = []

    tamanho_do_bloco = (85, 25)
    espaco_x = 10
    espaco_y = 10 

    largura_da_tela = tamanho_da_tela[0]
    largura_total_da_tela = (8 * (85)) + (7 * espaco_x)
    x_inicial = (largura_da_tela - largura_total_da_tela) // 2

    y_inicial = 50
