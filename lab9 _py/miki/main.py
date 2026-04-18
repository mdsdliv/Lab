import pygame
import datetime
import sys
import os

# Фикс путей для Mac
os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()

# --- 1. СНАЧАЛА СОЗДАЕМ ОКНО ---
# Задаем размер заранее, чтобы избежать ошибки "No video mode has been set"
SQUARE_SIZE = 800 
screen = pygame.display.set_mode((SQUARE_SIZE, SQUARE_SIZE))
pygame.display.set_caption("Mickey Clock Square")

# --- 2. ЗАГРУЗКА И КВАДРАТИЗАЦИЯ ФОНА ---
try:
    bg_raw = pygame.image.load('mickeybody.png').convert()
    # Масштабируем фон под наш квадрат
    mickey_bg = pygame.transform.scale(bg_raw, (SQUARE_SIZE, SQUARE_SIZE))
except Exception as e:
    print(f"Ошибка загрузки фона: {e}")
    pygame.quit()
    sys.exit()

# --- 3. НАСТРОЙКИ РУК (НОРМАЛЬНАЯ ТОЛЩИНА) ---
# Минута (lefthand) - чуть короче
SCALE_MIN = 0.42  
# Секунда (righthand) - чуть длиннее
SCALE_SEC = 0.52  

try:
    # Загружаем
    hand_min_raw = pygame.image.load('lefthand.png').convert_alpha()
    hand_sec_raw = pygame.image.load('righthand.png').convert_alpha()
    
    # Пропорционально масштабируем (чтобы не были слишком тонкими)
    hand_min_img = pygame.transform.scale(hand_min_raw, 
        (int(hand_min_raw.get_width() * SCALE_MIN), int(hand_min_raw.get_height() * SCALE_MIN)))
    
    hand_sec_img = pygame.transform.scale(hand_sec_raw, 
        (int(hand_sec_raw.get_width() * SCALE_SEC), int(hand_sec_raw.get_height() * SCALE_SEC)))
except Exception as e:
    print(f"Ошибка загрузки рук: {e}")
    pygame.quit()
    sys.exit()

def rotate_center(image, angle, correction):
    # Вращение строго по центру без смещений
    rotated = pygame.transform.rotozoom(image, -angle + correction, 1)
    rect = rotated.get_rect(center=(SQUARE_SIZE // 2, SQUARE_SIZE // 2))
    return rotated, rect

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = datetime.datetime.now()

    # ОТРИСОВКА
    screen.fill((0, 0, 0)) # Черный фон
    screen.blit(mickey_bg, (0, 0))

    # МИНУТЫ (lefthand.png)
    # Коррекция -90 обычно подходит для этих рук
    m_img, m_rect = rotate_center(hand_min_img, now.minute * 6, -90)
    screen.blit(m_img, m_rect)

    # СЕКУНДЫ (righthand.png)
    s_img, s_rect = rotate_center(hand_sec_img, now.second * 6, -90)
    screen.blit(s_img, s_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()