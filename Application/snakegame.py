import pygame
import random

# Initialize Pygame
pygame.init()

# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Set the screen size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

# Define the snake block size
block_size = 10
snake_speed = 15

# Define the starting position of the snake
def snake_position():
  snake_head = [screen_width / 2, screen_height / 2]
  snake_body = [[snake_head[0] - block_size, snake_head[1]], [snake_head[0] - 2*block_size, snake_head[1]]]
  return snake_head, snake_body

# Function to display the snake
def draw_snake(snake_body):
  for block in snake_body:
    pygame.draw.rect(screen, green, pygame.Rect(block[0], block[1], block_size, block_size))

# Function to display the message on the game screen
def display_message(msg, color):
  font_style = pygame.font.SysFont(None, 30)
  message = font_style.render(msg, True, color)
  screen.blit(message, [screen_width/6, screen_height/3])

# Function to handle game over
def game_loop():
  game_over = False
  game_close = False

  # Define starting position of the snake
  snake_head, snake_body = snake_position()

  # Define starting position of the food
  food_x = round(random.randrange(0, screen_width - block_size) / 10.0) * 10.0
  food_y = round(random.randrange(0, screen_height - block_size) / 10.0) * 10.0

  x_change = 0
  y_change = 0

  clock = pygame.time.Clock()

  while not game_over:

    while game_close:
      screen.fill(black)
      display_message("You Lost! Press Q - Quit or C - Play Again", red)
      pygame.display.update()

      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_q:
            game_over = True
          if event.key == pygame.K_c:
            game_loop()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        game_over = True
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT and x_change != block_size:
          x_change = -block_size
          y_change = 0
        elif event.key == pygame.K_RIGHT and x_change != -block_size:
          x_change = block_size
          y_change = 0
        elif event.key == pygame.K_UP and y_change != block_size:
          y_change = -block_size
          x_change = 0
        elif event.key == pygame.K_DOWN and y_change != -block_size:
          y_change = block_size

    snake_head[0] += x_change
    snake_head[1] += y_change

    screen.fill(black)
    pygame.draw.rect(screen, red, pygame.Rect(food_x, food_y, block_size, block_size))

    draw_snake(snake_body)

    pygame.display.update()

    # Check if the snake hits the border
    if snake_head[0] >= screen_width or snake_head[0] < 0 or snake_head[1] >= screen_height or snake_head[1] < 0:
      game_close
