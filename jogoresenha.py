from re import S
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720)) # configura janela do jogo
clock = pygame.time.Clock()
running = True
s = 1
jogar = pygame.image.load('jogar.png').convert_alpha()
jogar = pygame.transform.scale(jogar, (900, 720))
sair = pygame.image.load('sair.png').convert_alpha()
jogar_rect = jogar.get_rect()
jogar_rect.topleft = (146, 392)


while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if s == 1:
      background = pygame.image.load('inicio.png')
      background = pygame.transform.scale(background, (1280, 720))
      screen.blit(background, (0, 0))
      screen.blit(jogar, jogar_rect.topleft)
    elif s == 2:
      background = pygame.image.load('meio.png')
      background = pygame.transform.scale(background, (1280, 720))
    if event.type == pygame.MOUSEBUTTONDOWN:
      print(event.pos[0])
      print(event.pos[1])


  pygame.display.flip()

clock.tick(60)  # Pausa e indica a taxa de quadros por segundo (FPS)
pygame.quit()
