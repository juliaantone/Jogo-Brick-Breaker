import pygame
import sys
import random

pygame.init()
tamanho_da_tela = (800, 600)
tela = pygame.display.set_mode(tamanho_da_tela)
pygame.display.set_caption("BRICK BREAKER")
relogio = pygame.time.Clock()


cores = {
    "branco": (255, 255, 255),
    "lílas": (167, 139, 250),
    "roxo": (124, 58, 255),
    "roxo escuro": (107, 33, 168),
    "roxo claro": (196, 181, 253),
    "verde": (100, 220, 120),
    "verde escuro": (22, 101, 52),
    "azul escuro": (30, 64, 175)
}


fonte_do_titulo = pygame.font.SysFont("impact", 68)
fonte_do_botao = pygame.font.SysFont("arial bold", 36)
fonte_vidas_nivel = pygame.font.SysFont("times new roman", 24)
fonte_pontuacao = pygame.font.SysFont("times new roman", 42)

vidas = 5
nivel = 1
pontuacao = 0
bola_forte False
tempo_bola_forte = 0

tamanho_da_bola = 15
bola = pygame.Rect(100,375, tamanho_da_bola, tamanho_da_bola)
velocidade_da_bola = [5, -5]
barra_largura_padrao = 100
barra = pygame.Rect(0, 550, barra_largura_padrao, 15)


def criar_blocos(nivel): 
    blocos = []

    tamanho_do_bloco = (85, 25)
    espaco_x = 10
    espaco_y = 10 

    largura_da_tela = tamanho_da_tela[0]
    largura_total_da_tela = (8 * (85)) + (7 * espaco_x)
    x_inicial = (largura_da_tela - largura_total_da_tela) // 2
    y_inicial = 50

    if nivel == 1:
        resistencia = 1
    elif nivel == 2:
        resistencia = 1
    else:
        resistencia = 2


    for linha in range(5):
        for coluna in range(8):
            x = x_inicial + coluna * ((85) + espaco_x)
            y = y_inicial + linha * ((25) + espaco_y)

            bloco = pygame.Rect(x, y, (85), (25))
            blocos.append({
                "rect": bloco,
                "vida": resistencia
            })
    return blocos


def cor_dos_blocos(nivel):
    if nivel == 2:
        return cores["azul escuro"]
    if nivel == 3:
        return cores["verde escuro"]
    return cores["roxo escuro"]


tamanho_do_botao = (200, 60)
x_botao = (800) // 2 - (200) // 2
y_botao = 350
botao_jogar = pygame.Rect(x_botao, y_botao, (200), (60))


def tela_de_abertura():
    while True:
        tela.fill(cores["roxo claro"])

        texto_do_titulo = fonte_do_titulo.render("BRICK BREAKER", True, cores["roxo"])
        tela.blit(texto_do_titulo, ((800) // 2 - texto_do_titulo.get_width() // 2, 180))

        posicao_do_mouse = pygame.mouse.get_pos()
        mouse_clicado = pygame.mouse.get_pressed()

        if botao_jogar.collidepoint(posicao_do_mouse):
            pygame.draw.rect(tela, cores["lílas"], botao_jogar)
            if mouse_clicado[0]:
                return
        else:
            pygame.draw.rect(tela, cores["branco"], botao_jogar)

        texto_botao = fonte_do_botao.render("JOGAR", True, cores["roxo"])
        tela.blit(texto_botao,
            (
                botao_jogar.x + (200) // 2 - texto_botao.get_width() // 2,
                botao_jogar.y + (60) // 2 - texto_botao.get_height() // 2
            )
        )

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.flip()
        relogio.tick(60)
tela_de_abertura()


def movimentar_barra():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    barra.centerx = mouse_x
    
    if barra.left < 0:
        barra.left = 0
    if barra.right > 800:
        barra.right = 800

    
def bola_fora():
    global vidas
    vidas -= 1
    bola.centerx = 400
    bola.centery = 375
    velocidade_da_bola[0] = 5
    velocidade_da_bola[1] = -5


def movimentar_bola():
    global velocidade_da_bola
    bola.x += velocidade_da_bola[0]
    bola.y += velocidade_da_bola[1]

    if bola.left <= 0 or bola.right >= 800:
        velocidade_da_bola[0] *=-1
    if bola.top <= 0:
        velocidade_da_bola[1] *=-1
    if bola.colliderect(barra):
        velocidade_da_bola[1] *=-1
        bola.bottom = barra.top
    if bola.top > 600:
        bola_fora()
        if vidas <= 0:
            return  "acabou"


def desenhar_texto():
    texto_vidas = fonte_vidas_nivel.render(f"VIDAS: {vidas}", True, cores["roxo"])
    tela.blit( texto_vidas, (tamanho_da_tela[0] - texto_vidas.get_width() - 25,  10))

    texto_nivel = fonte_vidas_nivel.render(f"NÍVEL: {nivel}", True, cores["roxo"])
    tela.blit(texto_nivel, (25, 10))

tamanho_do_botao_jogar_novamente = (400, 60)
x_botao = (800) // 2 - (400) // 2
y_botao = 350 
botao_jogar_novamente = pygame.Rect(x_botao, y_botao, (400), (60))

def resetar_jogo():
    global vidas, pontuacao, nivel, velocidade_da_bola

    vidas = 5
    pontuacao = 0
    nivel = 1
    bola.centerx = 400
    bola.centery = 375
    velocidade_da_bola[0] = 5
    velocidade_da_bola[1] = -5
    barra.centerx = 400

poderes = []
velocidade_poderes = []

def criar_poderes(x, y):
    poderes = pygame.Rect(x, y, 20, 20)
    poderes.append(poderes)
    return

def tela_proximos_niveis():
    return


def tela_ganhou():
    while True:
        tela.fill(cores["roxo claro"])
         
        título = fonte_do_titulo.render("VOCÊ GANHOU!", True, cores["roxo"])
        tela.blit(título, ((800) // 2 - título.get_width() // 2, 180))

        posicao_do_mouse = pygame.mouse.get_pos()
        mouse_clicado = pygame.mouse.get_pressed()
        
        if botao_jogar_novamente.collidepoint(posicao_do_mouse):
            pygame.draw.rect(tela, cores["lílas"], botao_jogar_novamente)
            if mouse_clicado[0]:
                return 
        
        else:
            pygame.draw.rect(tela, cores["branco"], botao_jogar_novamente)

        pontos_texto = fonte_pontuacao.render(f"PONTUAÇÃO: {pontuacao}", True, cores["roxo escuro"])
        tela.blit(pontos_texto, (230, 280))

        texto_botao_jogar_novamente = fonte_do_botao.render("JOGAR NOVAMENTE", True, cores["roxo"])
        tela.blit(texto_botao_jogar_novamente,
            (
                      botao_jogar_novamente.x + (400) // 2 - texto_botao_jogar_novamente.get_width() // 2,
                      botao_jogar_novamente.y + (60) // 2 - texto_botao_jogar_novamente.get_height() // 2
            )
        )

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()
        relogio.tick(60)


def tela_perdeu():
    while True:
        tela.fill(cores["roxo claro"])
         
        título = fonte_do_titulo.render("VOCÊ PERDEU!", True, cores["roxo"])
        tela.blit(título, ((800) // 2 - título.get_width() // 2, 180))

        posicao_do_mouse = pygame.mouse.get_pos()
        mouse_clicado = pygame.mouse.get_pressed()
        
        if botao_jogar_novamente.collidepoint(posicao_do_mouse):
            pygame.draw.rect(tela, cores["lílas"], botao_jogar_novamente)
            if mouse_clicado[0]:
                return 
        
        else:
            pygame.draw.rect(tela, cores["branco"], botao_jogar_novamente)

        pontos_texto = fonte_pontuacao.render(f"PONTUAÇÃO: {pontuacao}", True, cores["roxo escuro"])
        tela.blit(pontos_texto, (230, 280))

        texto_botao_jogar_novamente = fonte_do_botao.render("JOGAR NOVAMENTE", True, cores["roxo"])
        tela.blit(texto_botao_jogar_novamente,
            (
                      botao_jogar_novamente.x + (400) // 2 - texto_botao_jogar_novamente.get_width() // 2,
                      botao_jogar_novamente.y + (60) // 2 - texto_botao_jogar_novamente.get_height() // 2
            )
        )

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()
        relogio.tick(60)

def tela_de_jogo(): 
        global nivel
        fim_jogo = False 
        blocos =  criar_blocos(nivel)

        while not fim_jogo:
            tela.fill(cores["branco"])

            desenhar_texto()
            estado = movimentar_bola()
            if estado == "acabou":
                tela_perdeu()
                return
            for bloco in blocos:
                if bola.colliderect(bloco["rect"]):
                    velocidade_da_bola[1] *= -1
                    bloco["vida"] -= 1

                    if bloco["vida"] <= 0:
                        blocos.remove(bloco)
                        global pontuacao
                        pontuacao +=10
                    break
            if len(blocos) == 0:
                if nivel == 1:
                    nivel = 2
                    tela_proximos_niveis()
                    blocos = criar_blocos(nivel)
                    bola.centerx = 400
                    bola.centery = 375
                    velocidade_da_bola[0] = 5
                    velocidade_da_bola[1] = -5
                    continue
                elif nivel == 2:
                    nivel = 3
                    tela_proximos_niveis()
                    blocos = criar_blocos(nivel)
                    bola.centerx = 400
                    bola.centery = 375
                    velocidade_da_bola[0] = 5
                    velocidade_da_bola[1] = -5
                    continue
                elif nivel == 3:
                    tela_ganhou()
                    return
            movimentar_barra()

            pygame.draw.rect(tela, cores["roxo"], barra)
            pygame.draw.rect(tela, cores["roxo"], bola)

            for bloco in blocos:
                pygame.draw.rect(tela, cor_dos_blocos(nivel), bloco["rect"])

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    fim_jogo = True
                
            pygame.display.flip()
            relogio.tick(60) 
while True:
    tela_de_abertura()
    resetar_jogo()
    tela_de_jogo()
    
pygame.quit()
sys.exit()