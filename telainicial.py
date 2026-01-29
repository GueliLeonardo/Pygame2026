from re import S
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720)) # configura janela do jogo
clock = pygame.time.Clock()
running = True
s = 1


while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if s == 1:
      background = pygame.image.load('inicio1.png')
      background = pygame.transform.scale(background, (1280, 720))
    elif s == 2:
      background = pygame.image.load('meio.png')
      background = pygame.transform.scale(background, (1280, 720))

    screen.blit(background, (0, 0))
  pygame.display.flip()

clock.tick(60)  # Pausa e indica a taxa de quadros por segundo (FPS)
pygame.quit()
