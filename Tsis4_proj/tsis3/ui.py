import pygame
import sys

WHITE, BLACK, GRAY = (255,255,255), (0,0,0), (200,200,200)

def draw_text(surf, text, size, x, y, color=BLACK):
    font = pygame.font.SysFont("Verdana", size)
    img = font.render(text, True, color)
    rect = img.get_rect(center=(x, y))
    surf.blit(img, rect)

def button(surf, text, x, y, w, h):
    mx, my = pygame.mouse.get_pos()
    clicked = pygame.mouse.get_pressed()[0]
    rect = pygame.Rect(x - w//2, y - h//2, w, h)
    color = (170, 170, 170) if rect.collidepoint(mx, my) else GRAY
    pygame.draw.rect(surf, color, rect)
    draw_text(surf, text, 20, x, y)
    return rect.collidepoint(mx, my) and clicked

def screen_username(surf, clock, w, h):
    name = ""
    while True:
        surf.fill(WHITE)
        draw_text(surf, "Enter Username:", 30, w//2, h//2 - 50)
        draw_text(surf, name + "_", 25, w//2, h//2, (0,0,255))
        draw_text(surf, "Press ENTER to start", 15, w//2, h//2 + 50)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and name: return name
                elif event.key == pygame.K_BACKSPACE: name = name[:-1]
                else: 
                    if len(name) < 10: name += event.unicode
        pygame.display.flip()
        clock.tick(30)

def screen_main_menu(surf, clock, w, h):
    while True:
        surf.fill(WHITE)
        draw_text(surf, "RACER ARCADE", 40, w//2, 100)
        if button(surf, "PLAY", w//2, 250, 200, 50): 
            pygame.time.delay(200); return "play"
        if button(surf, "LEADERBOARD", w//2, 320, 200, 50): 
            pygame.time.delay(200); return "leaderboard"
        if button(surf, "SETTINGS", w//2, 390, 200, 50): 
            pygame.time.delay(200); return "settings"
        if button(surf, "QUIT", w//2, 460, 200, 50): return "quit"
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return "quit"
        pygame.display.flip()
        clock.tick(30)

def screen_settings(surf, clock, w, h, settings):
    colors = ["Red", "Blue", "Green"]
    diffs = ["Normal", "Hard"]
    while True:
        surf.fill(WHITE)
        draw_text(surf, "SETTINGS", 35, w//2, 80)
        
        # Переключатель цвета
        draw_text(surf, f"Color: {settings['car_color']}", 20, w//2, 200)
        if button(surf, "Change Color", w//2, 240, 180, 40):
            idx = (colors.index(settings['car_color']) + 1) % len(colors)
            settings['car_color'] = colors[idx]
            pygame.time.delay(150)

        # Переключатель сложности
        draw_text(surf, f"Difficulty: {settings['difficulty']}", 20, w//2, 320)
        if button(surf, "Change Diff", w//2, 360, 180, 40):
            idx = (diffs.index(settings['difficulty']) + 1) % len(diffs)
            settings['difficulty'] = diffs[idx]
            pygame.time.delay(150)

        if button(surf, "SAVE & BACK", w//2, 500, 200, 50): return settings
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
        pygame.display.flip()
        clock.tick(30)

def screen_leaderboard(surf, clock, w, h, leaderboard):
    while True:
        surf.fill(WHITE)
        draw_text(surf, "TOP 10 SCORES", 30, w//2, 50)
        for i, entry in enumerate(leaderboard):
            txt = f"{i+1}. {entry['name']} - {entry['score']}"
            draw_text(surf, txt, 18, w//2, 120 + i*35)
        
        if button(surf, "BACK", w//2, 530, 150, 40): return
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
        pygame.display.flip()
        clock.tick(30)

def screen_game_over(surf, clock, w, h, score, distance, coins):
    while True:
        surf.fill((50, 0, 0))
        draw_text(surf, "CRASHED!", 50, w//2, 100, WHITE)
        draw_text(surf, f"Final Score: {score}", 25, w//2, 200, WHITE)
        draw_text(surf, f"Distance: {int(distance)}m", 20, w//2, 250, GRAY)
        
        if button(surf, "RETRY", w//2, 380, 180, 50): return "retry"
        if button(surf, "MENU", w//2, 450, 180, 50): return "menu"
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
        pygame.display.flip()
        clock.tick(30)