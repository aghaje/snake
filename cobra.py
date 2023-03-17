import pygame
import random

# Inicializando o Pygame
pygame.init()

# Definindo cores
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Definindo tamanho da tela
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

# Definindo tamanho da cobrinha e da comida
SNAKE_SIZE = FOOD_SIZE = 35

# Definindo velocidade inicial da cobrinha
SNAKE_SPEED = 8

# Criando a tela do jogo
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Criando a cobrinha
snake = pygame.Surface((SNAKE_SIZE,SNAKE_SIZE))
snake.fill(GREEN)

# Criando a comida
food = pygame.Surface((FOOD_SIZE, FOOD_SIZE))
food.fill(RED)

# Posição inicial da cobrinha e da comida
snake_position = [100,50]
food_position = [random.randrange(1,(SCREEN_WIDTH-FOOD_SIZE)//10)*10,
                 random.randrange(1,(SCREEN_HEIGHT-FOOD_SIZE)//10)*10]
food_spawned = True

# Direção inicial da cobrinha
direction = "RIGHT"

score=0

clock=pygame.time.Clock()

font=pygame.font.SysFont("monospace",35)
def game_over():
    screen.fill((0,0,0))
    game_over_text = font.render("Game Over!", True, RED)
    screen.blit(game_over_text,(SCREEN_WIDTH/2-100,SCREEN_HEIGHT/2-50))
    pygame.display.update()
    pygame.time.wait(3000)
    pygame.quit()
    quit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = "UP"
            elif event.key == pygame.K_DOWN:
                direction = "DOWN"
            elif event.key == pygame.K_LEFT:
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT:
                direction = "RIGHT"

    # Atualizando a posição da cobrinha
    if direction == "UP":
        snake_position[1] -= SNAKE_SPEED
    elif direction == "DOWN":
        snake_position[1] += SNAKE_SPEED
    elif direction == "LEFT":
        snake_position[0] -= SNAKE_SPEED
    elif direction == "RIGHT":
        snake_position[0] += SNAKE_SPEED

    # Verificando colisão com a comida
    if (pygame.Rect(snake_position[0],snake_position[1],SNAKE_SIZE,SNAKE_SIZE).colliderect(pygame.Rect(food_position[0],food_position[1],FOOD_SIZE,FOOD_SIZE))):
        food_spawned = False
        score+=1
        SNAKE_SPEED+=2

    # Gerando nova comida se necessário
    if not food_spawned:
        food_position = [random.randrange(1,(SCREEN_WIDTH-FOOD_SIZE)//10)*10,
                         random.randrange(1,(SCREEN_HEIGHT-FOOD_SIZE)//10)*10]
        food_spawned = True

    # Verificando colisão com as bordas da tela
    if (snake_position[0]<30 or snake_position[0]>SCREEN_WIDTH-30-SNAKE_SIZE or 
       snake_position[1]<30 or snake_position[1]>SCREEN_HEIGHT-30-SNAKE_SIZE):
       game_over()

   # Desenhando o fundo e a borda amarela da tela
    screen.fill(WHITE)
    border_rect=pygame.draw.rect(screen,YELLOW,(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), 50)

    # Desenhando a cobrinha e a comida na tela
    screen.blit(snake,(snake_position))
    screen.blit(food,(food_position))

    # Desenhando o placar na tela
    score_text=font.render(f"Score: {score}",True,(0,0,0))
    screen.blit(score_text,(5,5))

    # Atualizando a tela do jogo
    pygame.display.update()

    clock.tick(20)

pygame.quit()