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


fonte_do_titulo = pygame.font.SysFont("impact", 64)
fonte_do_botao = pygame.font.SysFont("arial bold", 32)

tamanho_do_botao = (200, 60)
x_botao = (800) // 2 - (200) // 2
y_botao = 350
botao_jogar = pygame.Rect(x_botao, y_botao, (200), (60))

def tela_inical():
    while True:
        tela.fill(cores["roxo claro"])

        texto_do_titulo = fonte_do_titulo.render("BRICK BREAKER", True, cores["roxo"])
        tela.blit(texto_do_titulo, ((800) // 2 - texto_do_titulo.get_width() // 2, 180))

        posicao_do_mouse = pygame.mouse.get_pos()
        mouse_clicado = pygame.mouse.get_pressed()