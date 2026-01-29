from re import S
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720)) # configura janela do jogo
clock = pygame.time.Clock()
running = True
s = 1
jogar = pygame.image.load('jogar.png').convert_alpha()
jogar = pygame.transform.scale(jogar, (350, 250))
sair = pygame.image.load('sair.png').convert_alpha()
sair = pygame.transform.scale(sair, (350, 250))
sair_rect = sair.get_rect()
sair_rect.topleft = (520, 400)
jogar_rect = jogar.get_rect()
jogar_rect.topleft = (120, 400)


while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if s == 1:
      background = pygame.image.load('inicio.png')
      background = pygame.transform.scale(background, (1280, 720))
      screen.blit(background, (0, 0))
      screen.blit(jogar, jogar_rect.topleft)
      screen.blit(sair, sair_rect.topleft)
      if event.type == pygame.MOUSEBUTTONDOWN:
        if sair_rect.collidepoint(event.pos):
          running = False
        elif jogar_rect.collidepoint(event.pos):
          s = 2
    elif s == 2:
      background = pygame.image.load('meio.png')
      background = pygame.transform.scale(background, (1280, 720))
      screen.blit(background, (0, 0))

  pygame.display.flip()

clock.tick(60)  # Pausa e indica a taxa de quadros por segundo (FPS)
pygame.quit()
