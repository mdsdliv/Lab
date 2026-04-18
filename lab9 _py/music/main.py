import pygame
import os
import sys

# 1. Инициализация Pygame и Микшера
pygame.init()
pygame.mixer.init()

# Настройки окна
W, H = 600, 400
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("KBTU Music Player")
font = pygame.font.SysFont("Arial", 24)
small_font = pygame.font.SysFont("Arial", 18)

# Фикс путей для Mac: работаем в папке скрипта
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Поиск музыки в папке 'music'
MUSIC_DIR = "music"
if not os.path.exists(MUSIC_DIR):
    os.makedirs(MUSIC_DIR)
    print(f"Папка {MUSIC_DIR} создана. Положи туда песни!")

playlist = [f for f in os.listdir(MUSIC_DIR) if f.endswith(('.mp3', '.wav'))]
current_index = 0
is_playing = False

def load_and_play():
    if playlist:
        track_path = os.path.join(MUSIC_DIR, playlist[current_index])
        pygame.mixer.music.load(track_path)
        pygame.mixer.music.play()
        return True
    return False

def draw_text(text, x, y, color=(255, 255, 255), active_font=font):
    img = active_font.render(text, True, color)
    screen.blit(img, (x, y))

running = True
clock = pygame.time.Clock()

while running:
    screen.fill((20, 20, 20)) # Глубокий темный фон
    
    # Заголовок и текущий трек
    draw_text("Music Player Control", 50, 30, (200, 200, 0))
    
    if playlist:
        current_track = playlist[current_index]
        draw_text(f"Track: {current_track}", 50, 100, (0, 255, 255))
    else:
        draw_text("Playlist is empty!", 50, 100, (255, 0, 0))

    # Статус
    status_text = "Status: Playing" if is_playing else "Status: Paused/Stopped"
    status_color = (0, 255, 0) if is_playing else (150, 150, 150)
    draw_text(status_text, 50, 150, status_color)

    # Инструкция
    draw_text("Keyboard Commands:", 50, 250, (100, 100, 100), small_font)
    draw_text("P: Play/Pause  |  S: Stop  |  N: Next  |  B: Back  |  Q: Quit", 50, 280, (180, 180, 180), small_font)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p: # Play / Pause
                if not is_playing:
                    if not pygame.mixer.music.get_busy():
                        load_and_play()
                    else:
                        pygame.mixer.music.unpause()
                    is_playing = True
                else:
                    pygame.mixer.music.pause()
                    is_playing = False
            
            elif event.key == pygame.K_s: # Stop
                pygame.mixer.music.stop()
                is_playing = False
            
            elif event.key == pygame.K_n: # Next
                if playlist:
                    current_index = (current_index + 1) % len(playlist)
                    load_and_play()
                    is_playing = True
            
            elif event.key == pygame.K_b: # Back (Previous)
                if playlist:
                    current_index = (current_index - 1) % len(playlist)
                    load_and_play()
                    is_playing = True
            
            elif event.key == pygame.K_q: # Quit
                running = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()