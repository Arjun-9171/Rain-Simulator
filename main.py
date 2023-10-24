import pygame, random
from pygame.locals import QUIT

pygame.init()
display_screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Rain droplets!')

class Droplet:
  def __init__(self, droplet_color, droplet_x, droplet_y, droplet_width, droplet_height):
    self.droplet_x = droplet_x
    self.droplet_y = droplet_y
    self.rect = pygame.Surface((droplet_width, droplet_height))
    self.rect.fill(droplet_color)

  def draw(self, display_screen):
     display_screen.blit(self.rect, (self.droplet_x, self.droplet_y))

lines = []

droplets = 10

for i in range(droplets):
   drop = Droplet('blue', random.randint(0, 640), random.randint(0, 480), 10, 40)
   lines.append(drop)

while True:
   for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
   pygame.display.update()