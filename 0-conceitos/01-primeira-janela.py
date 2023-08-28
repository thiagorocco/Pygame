import pygame
from pygame.locals import *
from sys import exit

#inicializando a biblioteca pygame
pygame.init()

#variáveis para os valores de largura, altura e título da janela
largura = 640
altura = 480
titulo = 'Meu Primeiro Jogo com Pygame'

#tela recebe display(tela) com as dimensões das variáveis largura e altura
tela = pygame.display.set_mode((largura, altura))
#Definindo um titulo para a tela de acordo com a variável titulo
pygame.display.set_caption(titulo)

#While vai executar infinitamente o método update de display até que seja
#executado o evento QUIT
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()