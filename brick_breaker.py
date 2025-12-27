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
fonte_do_botao = pygame.font.SysFont("arial", 32)

