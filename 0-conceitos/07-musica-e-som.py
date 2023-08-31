import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

### Inserindo música ao jogo
musica_de_fundo = pygame.mixer.music.load('assets/audio/BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play(-1)#-1 faz a música tocar em loop

### Inserindo som à colisão dos objetos - Precisa ser na extensão .wav
barulho_colisao = pygame.mixer.Sound('assets/audio/smw_coin.wav')

largura = 640
altura = 480
titulo = 'Meu Primeiro Jogo com Pygame'

#Posição aleatório do retangulo azul
x_azul = randint(40,600)
y_azul = randint(50,430)

### Variável para controlar os pontos que serão exibidos
pontos = 0
### Definindo a fonte
fonte = pygame.font.SysFont('Liberation Serif', 40, True, True)

# propriedades do retângulo
largRect = 40
altRect = 50
posRectX = (largura - largRect)//2
posRectY = (altura - altRect)//2
rgbRect = (255, 0, 0)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption(titulo)
#controlando os frames por segundo
relogio = pygame.time.Clock()

while True:
    #tick define o número de frames por segundo do jogo
    relogio.tick(30)

    #Texto para exibir os pontos
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True,(255,255,255))

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

    #Colisão
    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)
        #incremente pontos a cada colisão
        pontos += 1
        #som da colisão
        barulho_colisao.play()

    #exibindo o texto na tela   X , Y
    tela.blit(texto_formatado,(450,40))

    pygame.display.update()

    #pygame.fonts.get_fonts() lista as fontes do pygame