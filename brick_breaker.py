import pygame
import sys

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
fonte_vidas_nivel = pygame.font.SysFont("arial", 26)
fonte_pontuacao = pygame.font.SysFont("arial bold", 46)

vidas = 5
nivel = 1
pontuacao = 0

tamanho_da_bola = 15
bola = pygame.Rect(100,375, tamanho_da_bola, tamanho_da_bola)
velocidade_padrao = [5, -5]
barra_largura_padrao = 100
barra = pygame.Rect(0, 550, barra_largura_padrao, 15)


def criar_blocos(nivel): #amg eu termino essa função amanha
    blocos = []

    tamanho_do_bloco = (85, 25)
    espaco_x = 10
    espaco_y = 10 

    largura_da_tela = tamanho_da_tela[0]
    largura_total_da_tela = (8 * (85)) + (7 * espaco_x)
    x_inicial = (largura_da_tela - largura_total_da_tela) // 2









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
        tela.blit(
            texto_botao,
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

    for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

                pygame.display.flip()
            relogio.tick(60)


def movimentar_bola():
    pass




    for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

                pygame.display.flip()
            relogio.tick(60)


def tela_de_jogo(): 
        fim_jogo = False 

        while not fim_jogo:
            tela.fill(cores["branco"])
            pygame.draw.rect(tela, cores["lílas"], barra)
            pygame.draw.rect(tela, cores["roxo escuro"], bola)



            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    fim_jogo = True
                movimentar_barra()
            pygame.display.flip()
            relogio.tick(60)
tela_de_jogo()
pygame.quit()
sys.exit()