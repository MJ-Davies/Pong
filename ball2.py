import pygame
from random import randint
BLACK = (0, 0, 0)

class Ball2(pygame.sprite.Sprite):
  #Creating a ball sprite
  def __init__(self, colour, width, height):
    super().__init__()
  
  #Gets transparent background
    self.image = pygame.Surface([width, height])
    self.image.fill(BLACK)
    self.image.set_colorkey(BLACK)

    #Draw our rectangle (ball)
    pygame.draw.rect(self.image, colour, [0, 0, width, height])

    #declare velocity
    self.velocity = [randint(2, 3), randint(-2, 3)]

    #Fetch the rectangle
    self.rect = self.image.get_rect()

  def update(self):
    self.rect.x += self.velocity[0]
    self.rect.y += self.velocity[1]
  
  def bounce(self):
    self.velocity[0] = -self.velocity[0]
    self.velocity[1] = randint(-8, 8)