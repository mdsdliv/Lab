import pygame, random, sys

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Начальные настройки
snake_pos = [100, 50]
# Тело змейки — это список блоков. Изначально их 3.
snake_body = [[100, 50], [90, 50], [80, 50]]
food_pos = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
direction = 'RIGHT'
score = 0
level = 1
speed = 10

def get_random_food():
    while True:
        pos = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
        if pos not in snake_body:
            return pos

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN': direction = 'UP'
            if event.key == pygame.K_DOWN and direction != 'UP': direction = 'DOWN'
            if event.key == pygame.K_LEFT and direction != 'RIGHT': direction = 'LEFT'
            if event.key == pygame.K_RIGHT and direction != 'LEFT': direction = 'RIGHT'

    # Двигаем голову
    if direction == 'UP': snake_pos[1] -= 10
    if direction == 'DOWN': snake_pos[1] += 10
    if direction == 'LEFT': snake_pos[0] -= 10
    if direction == 'RIGHT': snake_pos[0] += 10

    # 1. Добавляем новую голову в список тела
    snake_body.insert(0, list(snake_pos))

    # 2. ПРОВЕРКА: Скушала ли змейка шарик?
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_pos = get_random_food()
        # ЗДЕСЬ МЫ НЕ УДАЛЯЕМ ХВОСТ -> ЗМЕЙКА ВЫРОСЛА!
        
        if score % 3 == 0:
            level += 1
            speed += 3
    else:
        # 3. Если еду не ели — удаляем последний сегмент хвоста, 
        # чтобы длина оставалась прежней
        snake_body.pop()

    # Столкновение со стенами
    if snake_pos[0] < 0 or snake_pos[0] > WIDTH-10 or snake_pos[1] < 0 or snake_pos[1] > HEIGHT-10:
        pygame.quit()
        sys.exit()

    # Самопересечение
    for block in snake_body[1:]:
        if snake_pos == block:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    # Рисуем все блоки змейки
    for pos in snake_body:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], 10, 10))
    
    # Рисуем еду
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(food_pos[0], food_pos[1], 10, 10))
    
    # UI: Счет и Уровень
    font = pygame.font.SysFont("Arial", 20)
    txt = font.render(f"Score: {score}  Level: {level}", True, (255, 255, 255))
    screen.blit(txt, (10, 10))

    pygame.display.flip()
    clock.tick(speed)