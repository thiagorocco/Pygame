import pygame
from pygame.locals import *
from sys import exit

class Linha:
    def __init__(self, tela, cor, posIniXY, posFimXY, larg):
        pygame.draw.line(tela, cor, posIniXY, posFimXY, larg)

pygame.init()

largura = 640
altura = 480
titulo = 'Meu Primeiro Jogo com Pygame'

# propriedades do retângulo
largRect = 40
altRect = 50
centro = (largura - largRect)/2
posRectX = centro
posRectY = 0
rgbRect = (255, 0, 0)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption(titulo)
#controlando os frames por segundo
relogio = pygame.time.Clock()

while True:
    #tick define o número de frames por segundo do jogo
    relogio.tick(30)

    #truque para não gerar o "rastro" do movimento
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    ## Desenhando na tela
    pygame.draw.rect( tela, rgbRect, (posRectX, posRectY, largRect, altRect))
    #incrementando Y para movimentar o objeto na vertical
    if posRectY >= altura:
        posRectY = 0
    posRectY += 10
    pygame.display.update()
