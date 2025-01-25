# Pygame шаблон - скелет для нового проекта Pygame
import pygame
from random import randint as rd
from player import Player
from enemy import Enemy

# РАЗМЕРЫ ОКОШКА
WIDTH = 800
HEIGHT = 600

FPS = 60

# Задаем цветаdw
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()


player = Player("./capibara.png", 100, 120, 200, 200)
zombie = Enemy("./zombie.png", 10, 40, 500, 300, 5)
zombie2 = Enemy("./zombie.png", 80, 70, 100, 100, 5)
# TODO Добавить второго противника, сделать следование за игроком


x = 0
# Цикл игры
running = True
while running:

    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, (x, 200, 50, 20))

    zombie.draw(screen)
    zombie.follow(player, 1)
    zombie2.draw(screen)
    zombie2.follow(player, 1)
    player.draw(screen)
    player.movemant()
    if x >= WIDTH + 20:
        x = -70
    # Держим цикл на правильной скорости
    clock.tick(FPS)

    # Управление

    pygame.display.update()
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

pygame.quit()


# домашка 21.12.2024
# TODO Сделать движение вверх-вниз через клавиши, сделать проверки на пересечение верхней границы, нижней, и левой границ
