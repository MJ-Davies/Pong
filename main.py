import pygame
from paddle import Paddle
from ball import Ball
from ball2 import Ball2

#initializes pygame module
pygame.init()

#Define colour constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#Scores
score_one = 0
score_two = 0

#Creates window
WINDOW_SIZE = (700, 500)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Pong")

#Creates Paddle objects
paddle_one = Paddle(WHITE, 10, 100)
paddle_one.rect.x = 20
paddle_one.rect.y = 200

paddle_two = Paddle(WHITE, 10, 100)
paddle_two.rect.x = 670
paddle_two.rect.y = 200

#Create ball objects
ball = Ball(WHITE, 10, 10)
ball2 = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 194
ball2.rect.x = 345
ball2.rect.y = 194

#List of sprites
all_sprites = pygame.sprite.Group()

#Add sprites to list
all_sprites.add(paddle_one)
all_sprites.add(paddle_two)
all_sprites.add(ball)
all_sprites.add(ball2)

#Initializes control variable
running = True

#Initializes Clock object
clock = pygame.time.Clock()

# -- Main Game Loop --
while running:

  # -- Main Event loop
  for event in pygame.event.get(): #Checks for user input
    if event.type == pygame.QUIT:
      running = False # Ends game Loop
  
  #Move paddles
  keys = pygame.key.get_pressed()
  if keys[pygame.K_w]:
    paddle_one.move_up(5)
  if keys[pygame.K_s]:
    paddle_one.move_down(5)
  if keys[pygame.K_UP]:
    paddle_two.move_up(5)
  if keys[pygame.K_DOWN]:
    paddle_two.move_down(5)
  
  # -- Game Logic
  all_sprites.update()

  #Detects wall collision of ball
  if ball.rect.x >= 690:
    ball.velocity[0] = -ball.velocity[0]
    score_one += 1
    ball.rect.x = 345
    ball.rect.y = 194
  if ball.rect.x <= 0:
    ball.velocity[0] = -ball.velocity[0]
    score_two += 1
    ball.rect.x = 345
    ball.rect.y = 194

  if ball.rect.y > 490:
    ball.velocity[1] = -ball.velocity[1]
  if ball.rect.y < 0:
    ball.velocity[1] = -ball.velocity[1]
  
  #Detects wall collision of ball2
  if ball2.rect.x >= 690:
    ball2.velocity[0] = -ball2.velocity[0]
    score_one += 1
    ball2.rect.x = 345
    ball2.rect.y = 194
  if ball2.rect.x <= 0:
    ball2.velocity[0] = -ball2.velocity[0]
    score_two += 1
    ball2.rect.x = 345
    ball2.rect.y = 194

  if ball2.rect.y > 490:
    ball2.velocity[1] = -ball2.velocity[1]
  if ball2.rect.y < 0:
    ball2.velocity[1] = -ball2.velocity[1]
  
  #Detects paddle and ball collison
  if (pygame.sprite.collide_mask(ball, paddle_one)) or (pygame.sprite.collide_mask(ball, paddle_two)):
    ball.bounce()
  if (pygame.sprite.collide_mask(ball2, paddle_one)) or (pygame.sprite.collide_mask(ball2, paddle_two)):
    ball2.bounce()

  #Collision of ball 1 and ball2
  if (pygame.sprite.collide_mask(ball, ball2)):
    ball.bounce()
    ball2.bounce()

  # -- Drawing Code
  screen.fill(BLACK)
  pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
  all_sprites.draw(screen)

  #Displays scores
  font = pygame.font.Font(None, 74)
  text = font.render(str(score_one), 1, WHITE)
  screen.blit(text, (250, 10))

  text = font.render(str(score_two), 1, WHITE)
  screen.blit(text, (420, 10))
  
  # Update the screen
  pygame.display.flip()
  clock.tick(60)