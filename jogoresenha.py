from re import S
import pygame as pg
import math
import time

pg.init()
screen = pg.display.set_mode((1280, 720)) # configura janela do jogo
clock = pg.time.Clock()
running = True
s = 1
cash = 0
life = 1
round = 1
g = 0
i = 0
path = [(3, 275), (642,275 ), (642, 109), (413, 109), (413, 530), (178, 530), (178, 370), (824, 365), (824, 170), (955, 170), (955, 515), (643, 515), (643, 780)]
balaov_img = pg.image.load("fotos/rb.png").convert_alpha()

class oppv(pg.sprite.Sprite):
    def __init__(self, path, image):
        super().__init__()
        self.path = path
        self.index = 0
        self.x, self.y = path[0]
        self.speed = 1
        self.image = image
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.dano = 1
        self.reached_end = False

        self.max_health = 30
        self.health = self.max_health
        self.alive = True

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.alive = False

    def move(self):
        if self.index >= len(self.path) - 1:
            self.reached_end=True
            self.alive = False
            return

        target_x, target_y = self.path[self.index + 1]

        dx = target_x - self.x
        dy = target_y - self.y
        distance = math.hypot(dx, dy)

        if distance < self.speed:
            self.x, self.y = target_x, target_y
            self.index += 1
        else:
            self.x += (dx / distance) * self.speed
            self.y += (dy / distance) * self.speed

        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

balao = pg.sprite.Group()
balaov = oppv(path, pg.image.load("fotos/rb.png"))
balao.add(balaov)
def spawn_balaov():
    balaov = oppv(path, pg.image.load("fotos/rb.png"))
    balao.add(balaov)


font = pg.font.Font('fotos/Pixel.ttf', 40)
font2 = pg.font.Font('fotos/Pixel.ttf', 24)

textor = font.render(f"Round {round}", True, 'white')
textov = font2.render(f"{life}", True, 'white')
textoc = font2.render(f"{cash}", True, 'white')

jogar = pg.image.load('fotos/jogar.png').convert_alpha()
jogar = pg.transform.scale(jogar, (350, 250))
sair = pg.image.load('fotos/sair.png').convert_alpha()
sair = pg.transform.scale(sair, (350, 250))
sair_rect = sair.get_rect()
sair_rect.topleft = (520, 400)
jogar_rect = jogar.get_rect()
jogar_rect.topleft = (120, 400)


while running:
    
  for event in pg.event.get():
    if event.type == pg.QUIT:
      running = False

            
  if s == 1:
    background = pg.image.load('fotos/inicio.png')
    background = pg.transform.scale(background, (1280, 720))
    screen.blit(background, (0, 0))
    screen.blit(jogar, jogar_rect.topleft)
    screen.blit(sair, sair_rect.topleft)
    if event.type == pg.MOUSEBUTTONDOWN:
      if sair_rect.collidepoint(event.pos):
        running = False
      elif jogar_rect.collidepoint(event.pos):
        s = 2
  elif s == 2:
    background = pg.image.load('fotos/meio.png')
    background = pg.transform.scale(background, (1280, 720))
    for event in pg.event.get():
      if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and balaov.rect.collidepoint(event.pos):
        balaov.take_damage(10)
        print( 'bateu')
      if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
          spawn_balaov()

    for balaov in list(balao):
      balaov.move()

      if balaov.reached_end:
        life -= balaov.dano
        balao.remove(balaov)
        continue

      if not balaov.alive:
          balao.remove(balaov)

    screen.blit(background, (0, 0))
    screen.blit(textor, (350, 10))
    if life > 99:
      screen.blit(textov, (1146, 525))
    elif life > 9:
      screen.blit(textov, (1156, 525))
    elif life > 0:
      screen.blit(textov, (1176, 525))
    else:
        s = 3
    if cash > 99:
      screen.blit(textoc, (1146, 675))
    elif cash > 9:
      screen.blit(textoc, (1156, 675))
    elif cash >= 0:
      screen.blit(textoc, (1176, 675))
    balaov.move()
    balao.update()
    balao.draw(screen)
  elif s == 3:
    background = pg.image.load('fotos/fim.png')
    background = pg.transform.scale(background, (1280, 720))
    screen.blit(background, (0, 0))
    
    
    
  pg.display.flip()

clock.tick(60)  # Pausa e indica a taxa de quadros por segundo (FPS)
pg.quit()
