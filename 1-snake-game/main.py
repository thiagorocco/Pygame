'''
    Neste código pegaremos o último código desenvolvido no diretório conceitos.
    Vamos renomear as variáveis ret_vermelho e ret_azul para cobra e maca(maçã)
'''
import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

### Inserindo música ao jogo
pygame.mixer.music.set_volume(0.25)
musica_de_fundo = pygame.mixer.music.load('assets/audio/BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play(-1)#-1 faz a música tocar em loop

### Inserindo som à colisão dos objetos - Precisa ser na extensão .wav
barulho_colisao = pygame.mixer.Sound('assets/audio/smw_coin.wav')
barulho_colisao.set_volume(1)
largura = 640
altura = 480
titulo = 'Jogo da Cobrinha(Snake Game) com Pygame'

#Posição aleatório do retangulo azul
x_maca = randint(40,600)
y_maca = randint(50,430)
rgbMaca = (255, 0, 0)

### Variável para controlar os pontos que serão exibidos
pontos = 0
### Definindo a fonte
fonte = pygame.font.SysFont('Liberation Serif', 40, True, True)

# propriedades do retângulo
largCobra = 40
altCobra = 50
x_cobra = (largura - largCobra)//2
y_cobra = (altura - altCobra)//2
rgbCobra = (10, 255, 0)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption(titulo)
#controlando os frames por segundo
relogio = pygame.time.Clock()

while True:
    #tick define o número de frames por segundo do jogo
    relogio.tick(30)

    #Texto para exibir os pontos
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True,(0,0,0))

    #truque para não gerar o "rastro" do movimento
    tela.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if pygame.key.get_pressed()[K_a]:
        x_cobra -= 20
    if pygame.key.get_pressed()[K_d]:
        x_cobra += 20
    if pygame.key.get_pressed()[K_w]:
        y_cobra -= 20
    if pygame.key.get_pressed()[K_s]:
        y_cobra += 20

    ## Desenhando na tela
    cobra = pygame.draw.rect( tela, rgbCobra, (x_cobra, y_cobra, largCobra, altCobra))
    #posição x e y do azul será sempre uma surpresa
    maca = pygame.draw.rect( tela, rgbMaca, (x_maca, y_maca, 40, 50))

    #Colisão
    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        #incremente pontos a cada colisão
        pontos += 1
        #som da colisão
        barulho_colisao.play()

    #exibindo o texto na tela   X , Y
    tela.blit(texto_formatado,(450,40))

    pygame.display.update()

    #pygame.fonts.get_fonts() lista as fontes do pygame