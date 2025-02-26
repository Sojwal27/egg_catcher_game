import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Egg Catcher")

# Game variables
score = 0
missed_eggs = 0

# Egg properties
egg_image = pygame.image.load("egg.png")
egg_x = random.randint(0, 736)
egg_y = 50
egg_y_change = 5

# Basket properties
basket_image = pygame.image.load("basket.png")
basket_x = 370
basket_y = 480
basket_x_change = 0

def basket(x, y):
	screen.blit(basket_image, (x, y))

def egg(x, y):
    screen.blit(egg_image, (x, y))

running = True
while running:
    screen.fill((255, 255, 255))
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_LEFT:
        basket_x_change = -5
if event.key == pygame.K_RIGHT:
    basket_x_change = 5
if event.type == pygame.KEYUP:
    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        basket_x_change = 0

basket_x += basket_x_change
egg_y += egg_y_change

if egg_y > 600:
    egg_y = 50
egg_x = random.randint(0, 736)
missed_eggs += 1

if basket_x <= egg_x <= basket_x + 64 and basket_y <= egg_y <= basket_y + 64:
    score += 1
egg_y = 50
egg_x = random.randint(0, 736)

basket(basket_x, basket_y)
egg(egg_x, egg_y)
pygame.display.update()