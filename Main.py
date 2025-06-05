from Recursos.funcoes import limpar_tela, aguarde
import pygame, datetime, speech_recognition, pyttsx3

pygame.init()

LARGURA_TELA = 1000
ALTURA_TELA = 700
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Combate Cosmico")

# Carregamento de imagens
fundoJogo = pygame.image.load("Arquivos/fundo_Jogo.jpeg")
Inimigo = pygame.image.load("Arquivos/naveInimigo.png")
NaveJogador = pygame.image.load("Arquivos/navePlayer.png")


branco = (255, 255, 255)
preto = (0, 0, 0)


posicaoNaveX = 450
posicaoNaveY = 550
movimentoNaveX = 0


rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                movimentoNaveX = 0.5
            elif evento.key == pygame.K_LEFT:
                movimentoNaveX = -0.5
        elif evento.type == pygame.KEYUP:
            if evento.key in (pygame.K_RIGHT, pygame.K_LEFT):
                movimentoNaveX = 0

    
    posicaoNaveX += movimentoNaveX

    
    if posicaoNaveX < 0:
        posicaoNaveX = 0
    elif posicaoNaveX > 900: 
        posicaoNaveX = 900

    
    tela.blit(fundoJogo, (0, 0))
    for x in range(110, 901, 110):
        tela.blit(Inimigo, (x, 50))
    tela.blit(NaveJogador, (posicaoNaveX, posicaoNaveY))


    
    pygame.display.flip()


pygame.quit()