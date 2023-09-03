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
musica_de_fundo = pygame.mixer.music.load('assets/audio/happy_arcade.mp3')
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

corRgbMaca = (255, 0, 0)

### Variável para controlar os pontos que serão exibidos
pontos = 0
### Definindo a fonte
fonte = pygame.font.SysFont('Liberation Serif', 40, True, True)

# propriedades do retângulo
largCobra = 30
altCobra = 30
x_cobra = (largura - largCobra)//2
y_cobra = (altura - altCobra)//2
corRgbCobra = (10, 255, 0)

velocidade = 10
x_controle = velocidade
y_controle = 0

corRgbTela = (255,255,255)
corRgbTexto = (0,0,0)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption(titulo)
#controlando os frames por segundo
relogio = pygame.time.Clock()

#array do crescimento da cobra
lista_cobra = []
comprimento_inicial_cobra = 5

#Fazer o cobra crescer
def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        '''
            Para entendimento
            XeY = [x, y]
            XeY[0] = x
            XeY[1] = y
        '''
        pygame.draw.rect(tela, corRgbCobra, (XeY[0], XeY[1], largCobra, altCobra))
def reiniciar_jogo():
    global pontos, comprimento_inicial_cobra, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_maca, y_maca, morreu
    pontos = 0
    comprimento_inicial_cobra = 5
    x_cobra = int(largura/2)
    y_cobra = int(altura/2)
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(40,600)
    y_maca = randint(50,430)
    morreu = False
    pygame.mixer.music.play(-1)

while True:
    #tick define o número de frames por segundo do jogo
    relogio.tick(30)
    tela.fill(corRgbTela)

    #Texto para exibir os pontos
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True,corRgbTexto)

    #truque para não gerar o "rastro" do movimento
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        #Controlando movimentação, velocidade e bloquear
        #o pressionamento de teclas de direções opostas ao mesmo tempo
        if event.type == KEYDOWN:
           if event.key == K_a:
               if x_controle == velocidade:
                   pass
               else:
                    x_controle = -velocidade
                    y_controle = 0
           if event.key == K_d:
               if x_controle == -velocidade:
                   pass
               else:
                    x_controle = velocidade
                    y_controle = 0
           if event.key == K_w:
               if y_controle == velocidade:
                   pass
               else:
                    x_controle = 0
                    y_controle = -velocidade
           if event.key == K_s:
               if y_controle == -velocidade:
                   pass
               else:
                    x_controle = 0
                    y_controle = velocidade

    x_cobra += x_controle
    y_cobra += y_controle

    ## Desenhando na tela
    cobra = pygame.draw.rect( tela, corRgbCobra, (x_cobra, y_cobra, largCobra, altCobra))
    #posição x e y do azul será sempre uma surpresa
    maca = pygame.draw.rect( tela, corRgbMaca, (x_maca, y_maca, 30, 30))

    #Colisão
    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        #incremente pontos a cada colisão
        pontos += 1
        #som da colisão
        barulho_colisao.play()
        comprimento_inicial_cobra += 1

    #incrementando o tamanho da cobra
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    lista_cobra.append(lista_cabeca)

    #Verifica se a cobra colidiu nela mesma
    #Verifica se há mais de duas posições de cabeça na lista_cobra, se houver é verdadeiro
    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont(None,20,True,True)
        mensagem = 'Game Over! Pressione a tecla R para jogar novamente'
        texto_formatado = fonte2.render(mensagem, True, (0, 0, 0))
        ret_texto = texto_formatado.get_rect()
        pygame.mixer.music.stop()
        morreu = True
        while morreu:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
            ret_texto.center = (largura//2,altura//2)
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()


    if len(lista_cobra) > comprimento_inicial_cobra:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)

    #exibindo o texto na tela   X , Y
    tela.blit(texto_formatado,(50,40))

    pygame.display.update()

    #pygame.fonts.get_fonts() lista as fontes do pygame