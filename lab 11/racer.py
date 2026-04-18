
import pygame, sys, random, time
from pygame.locals import *

pygame.init()
FPS = 60
FramePerSec = pygame.time.Clock()

# Настройки
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 600
SPEED = 5        # Начальная скорость врага
SCORE = 0        # Пройденные враги
COIN_SCORE = 0   # Собранные монеты
N = 5            # Каждые N монет скорость растет

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer Pro")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.Surface((50, 80))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED) # Используем общую скорость SPEED
        if (self.rect.top > SCREEN_HEIGHT):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Генерируем случайный вес: 1 (обычная) или 3 (золотая)
        self.weight = random.choice([1, 3])
        self.image = pygame.Surface((20, 20))
        # Золотая монета — желтая, обычная — серая
        self.image.fill((255, 215, 0) if self.weight == 3 else (192, 192, 192))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        self.rect.move_ip(0, 5) # Монеты падают с постоянной скоростью
        if self.rect.top > SCREEN_HEIGHT:
            self.kill() # Удаляем, если улетела за экран

# Группы спрайтов
P1 = pygame.sprite.Sprite() # Игрок (упрощенно)
P1.image = pygame.Surface((40, 70)); P1.image.fill((0,0,255))
P1.rect = P1.image.get_rect(); P1.rect.center = (200, 500)

enemies = pygame.sprite.Group(); E1 = Enemy(); enemies.add(E1)
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group(); all_sprites.add(P1); all_sprites.add(E1)

# Таймер для генерации монет
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 2000) # Новая монета каждые 2 сек

while True:
    for event in pygame.event.get():
        if event.type == QUIT: pygame.quit(); sys.exit()
        if event.type == INC_SPEED:
            new_coin = Coin()
            coins.add(new_coin); all_sprites.add(new_coin)

    # Движение игрока
    keys = pygame.key.get_pressed()
    if keys[K_LEFT] and P1.rect.left > 0: P1.rect.move_ip(-5, 0)
    if keys[K_RIGHT] and P1.rect.right < SCREEN_WIDTH: P1.rect.move_ip(5, 0)

    DISPLAYSURF.fill((255, 255, 255))
    
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        if entity != P1: entity.move()

    # Сбор монет
    collided_coins = pygame.sprite.spritecollide(P1, coins, True)
    for c in collided_coins:
        COIN_SCORE += c.weight
        # Ускорение врага при наборе N монет
        if COIN_SCORE >= N:
            SPEED += 1 # Враг становится быстрее
            COIN_SCORE = 0 # Сбрасываем счетчик для следующего ускорения

    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.quit(); sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)
