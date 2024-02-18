import pygame
BLACK = (0, 0, 0)

class Paddle(pygame.sprite.Sprite):
  def __init__(self, colour, width, height):

    #Initializes properties and methods from parent class
    super().__init__()

    #Initialize background colour
    self.image = pygame.Surface([width, height])
    self.image.fill(BLACK)
    self.image.set_colorkey(BLACK)

    #Draw our paddle
    pygame.draw.rect(self.image, colour, [0,0, width, height])

    #Fetch the rectangle | creates hitbox
    self.rect = self.image.get_rect()

  def move_up(self, pixels):
    self.rect.y -= pixels

    #check if paddle is not going off screen
    if self.rect.y < 0:
      self.rect.y = 0
    
  def move_down(self, pixels):
    self.rect.y += pixels

    #check if paddle is not going off screen
    if self.rect.y > 400:
      self.rect.y = 400