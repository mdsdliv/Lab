import pygame
import random

W, H = 400, 600
LANES = [60, 150, 250, 340]

class Player(pygame.sprite.Sprite):
    def __init__(self, color_name):
        super().__init__()
        self.image = pygame.Surface((40, 70))
        self.image.fill(pygame.Color(color_name))
        self.rect = self.image.get_rect(center=(200, 500))
        self.speed = 7
        self.shield = False

class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.image = pygame.Surface((40, 70))
        self.image.fill((200, 0, 0))
        self.rect = self.image.get_rect(center=(random.choice(LANES), -100))
        self.speed = speed
    def update(self):
        self.rect.y += self.speed
        if self.rect.top > H: self.kill()

class Item(pygame.sprite.Sprite):
    def __init__(self, itype, color):
        super().__init__()
        self.itype = itype
        self.image = pygame.Surface((30, 30))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(random.choice(LANES), -50))
    def update(self, speed):
        self.rect.y += speed
        if self.rect.top > H: self.kill()

def run_game(surf, clock, settings, username):
    player = Player(settings.get("car_color", "Red"))
    enemies = pygame.sprite.Group()
    items = pygame.sprite.Group()
    
    score, coins, distance = 0, 0, 0.0
    speed = 5 if settings["difficulty"] == "Normal" else 8
    nitro_timer = 0
    font = pygame.font.SysFont("Verdana", 20)

    while True:
        dt = clock.tick(60)
        surf.fill((100, 100, 100)) # Дорога
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return "menu", 0, 0, 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: return "menu", score, distance, coins

        # Движение
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.rect.left > 0: player.rect.x -= player.speed
        if keys[pygame.K_RIGHT] and player.rect.right < W: player.rect.x += player.speed

        # Спавн
        if random.randint(1, 60) == 1: enemies.add(Enemy(speed))
        if random.randint(1, 150) == 1: 
            it = random.choice([("coin", (255,215,0)), ("nitro", (0,0,255)), ("shield", (0,255,255))])
            items.add(Item(it[0], it[1]))

        # Обновление логики
        eff_speed = speed * 2 if nitro_timer > pygame.time.get_ticks() else speed
        enemies.update()
        items.update(eff_speed)
        distance += eff_speed / 100

        # Коллизии
        if pygame.sprite.spritecollide(player, enemies, True):
            if player.shield: player.shield = False
            else: return "dead", int(distance * 10 + coins * 50), distance, coins

        for hit in pygame.sprite.spritecollide(player, items, True):
            if hit.itype == "coin": coins += 1
            elif hit.itype == "nitro": nitro_timer = pygame.time.get_ticks() + 3000
            elif hit.itype == "shield": player.shield = True

        # Отрисовка
        enemies.draw(surf)
        items.draw(surf)
        surf.blit(player.image, player.rect)
        if player.shield: pygame.draw.rect(surf, (0,255,255), player.rect, 3)
        
        score_text = font.render(f"Score: {int(distance * 10 + coins * 50)}", True, (255,255,255))
        surf.blit(score_text, (10, 10))
        
        pygame.display.flip()