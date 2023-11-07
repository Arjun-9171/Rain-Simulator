import pygame, random, time
from pygame.locals import QUIT

pygame.init()
pygame.mixer.init()
display_screen = pygame.display.set_mode((1760, 990))
pygame.display.set_caption('Rain droplets!')
background = pygame.image.load('fondo.png')
rain_sound = pygame.mixer.Sound("Rain.mp3")
background = pygame.transform.scale(background, (1760, 990))
class Droplet:
   def __init__(self, droplet_color, droplet_x, droplet_y, droplet_width, droplet_height):
      self.droplet_x = droplet_x
      self.droplet_y = droplet_y
      self.rect = pygame.Surface((droplet_width, droplet_height))
      self.rect.fill(droplet_color)
   
   def draw(self, display_screen):
      display_screen.blit(self.rect, (self.droplet_x, self.droplet_y))

   def update(self):
      self.droplet_y = self.droplet_y + 1
      if self.droplet_y >= 990:
         self.droplet_y = 0
      

lines = []

droplets = 1000

for i in range(droplets):
   drop = Droplet('blue', random.randint(0, 1760), random.randint(0, 990), 10, 40)
   lines.append(drop)

rain_sound.play()
while True:
   
   for event in pygame.event.get():
      if event.type == QUIT:
         pygame.quit()
   display_screen.blit(background, (0, 0))
   for index in range(droplets):
      lines[index].draw(display_screen)
      lines[index].update()
   #drop.draw(display_screen)
   #drop.update()
   pygame.display.update()
   time.sleep(0.001)