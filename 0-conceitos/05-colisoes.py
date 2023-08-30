import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 640
altura = 480
titulo = 'Meu Primeiro Jogo com Pygame'

#Posição aleatório do retangulo azul
x_azul = randint(40,600)
y_azul = randint(50,430)

# propriedades do retângulo
largRect = 40
altRect = 50
posRectX = (largura - largRect)/2
posRectY = (altura - altRect)/2
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

    if pygame.key.get_pressed()[K_a]:
        posRectX -= 20
    if pygame.key.get_pressed()[K_d]:
        posRectX += 20
    if pygame.key.get_pressed()[K_w]:
        posRectY -= 20
    if pygame.key.get_pressed()[K_s]:
        posRectY += 20

    ## Desenhando na tela
    ret_vermelho = pygame.draw.rect( tela, rgbRect, (posRectX, posRectY, largRect, altRect))
    #posição x e y do azul será sempre uma surpresa
    ret_azul = pygame.draw.rect( tela, (0,0,255), (x_azul, y_azul, 40, 50))

    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)

    pygame.display.update()
