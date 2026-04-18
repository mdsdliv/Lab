import pygame
import sys

# Инициализация
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Pygame Paint")
clock = pygame.time.Clock()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Переменные рисования
current_color = BLUE
mode = 'brush' # Режимы: 'brush', 'rect', 'circle', 'eraser'
canvas_color = WHITE

# Очистка экрана (холста) в начале
screen.fill(canvas_color)

def draw_menu():
    # Рисуем серую панель меню слева
    pygame.draw.rect(screen, GRAY, (0, 0, 100, HEIGHT))
    pygame.draw.line(screen, BLACK, (100, 0), (100, HEIGHT), 2)

    # Кнопки выбора цвета
    colors = [RED, GREEN, BLUE, YELLOW, BLACK]
    for i, color in enumerate(colors):
        rect = pygame.Rect(25, 20 + i * 45, 50, 40)
        pygame.draw.rect(screen, color, rect)
        if current_color == color and mode != 'eraser':
            pygame.draw.rect(screen, WHITE, rect, 3) # Подсветка активного цвета

    # Кнопки инструментов (текст)
    font = pygame.font.SysFont("Arial", 14, bold=True)
    
    # Кнопка Ластик
    eraser_rect = pygame.Rect(10, 300, 80, 40)
    pygame.draw.rect(screen, WHITE if mode == 'eraser' else (150, 150, 150), eraser_rect)
    screen.blit(font.render("ERASER", True, BLACK), (20, 312))

    # Кнопка Прямоугольник
    rect_tool = pygame.Rect(10, 350, 80, 40)
    pygame.draw.rect(screen, WHITE if mode == 'rect' else (150, 150, 150), rect_tool)
    screen.blit(font.render("RECT", True, BLACK), (30, 362))

    # Кнопка Круг
    circle_tool = pygame.Rect(10, 400, 80, 40)
    pygame.draw.rect(screen, WHITE if mode == 'circle' else (150, 150, 150), circle_tool)
    screen.blit(font.render("CIRCLE", True, BLACK), (25, 412))

    # Кнопка Кисть
    brush_tool = pygame.Rect(10, 450, 80, 40)
    pygame.draw.rect(screen, WHITE if mode == 'brush' else (150, 150, 150), brush_tool)
    screen.blit(font.render("BRUSH", True, BLACK), (25, 462))

    return colors, eraser_rect, rect_tool, circle_tool, brush_tool

while True:
    # Отрисовка меню каждую итерацию
    color_buttons, eraser_btn, rect_btn, circle_btn, brush_btn = draw_menu()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            
            # 1. Проверяем клики по меню
            if mouse_pos[0] < 100:
                # Клик по цветам
                for i, color in enumerate(color_buttons):
                    if pygame.Rect(25, 20 + i * 45, 50, 40).collidepoint(mouse_pos):
                        current_color = color
                        mode = 'brush' # При выборе цвета переключаем на кисть
                
                # Клик по инструментам
                if eraser_btn.collidepoint(mouse_pos): mode = 'eraser'
                if rect_btn.collidepoint(mouse_pos): mode = 'rect'
                if circle_btn.collidepoint(mouse_pos): mode = 'circle'
                if brush_btn.collidepoint(mouse_pos): mode = 'brush'
            
            # 2. Рисование фигур (одиночный клик)
            else:
                draw_color = canvas_color if mode == 'eraser' else current_color
                if mode == 'rect':
                    pygame.draw.rect(screen, draw_color, (mouse_pos[0]-25, mouse_pos[1]-25, 50, 50))
                elif mode == 'circle':
                    pygame.draw.circle(screen, draw_color, mouse_pos, 25)

    # 3. Рисование кистью (зажатая мышь)
    if pygame.mouse.get_pressed()[0]:
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[0] > 105: # Рисуем только вне зоны меню
            draw_color = canvas_color if mode == 'eraser' else current_color
            radius = 20 if mode == 'eraser' else 8
            pygame.draw.circle(screen, draw_color, mouse_pos, radius)

    pygame.display.flip()
    clock.tick(120)