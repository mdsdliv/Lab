import pygame
import sys
from datetime import datetime
from tool import (
    BRUSH_SIZES,
    draw_pencil, draw_line,
    draw_rectangle, draw_circle,
    draw_square, draw_right_triangle,
    draw_equilateral_triangle, draw_rhombus,
    draw_eraser, flood_fill,
)

SCREEN_W, SCREEN_H = 1100, 700
TOOLBAR_W          = 180
CANVAS_X           = TOOLBAR_W
CANVAS_W           = SCREEN_W - TOOLBAR_W
CANVAS_H           = SCREEN_H

# ТЕМНО-СИНИЙ ФОН
CANVAS_DEFAULT_BG = (25, 25, 112) 
TOOLBAR_BG   = (30, 30, 40)
WHITE        = (255, 255, 255)
ACCENT       = (100, 180, 255)

PALETTE = [
    (0,0,0),(255,255,255),(200,50,50),(50,180,50),
    (50,80,220),(255,200,0),(200,100,0),(160,0,200),
    (0,200,200),(255,120,180),(100,100,100),(200,200,200),
]

TOOLS = [
    "pencil","line","rectangle","circle",
    "square","right_triangle","equil_triangle","rhombus",
    "eraser","fill","text",
]

TOOL_LABELS = {
    "pencil": "✏ Pencil", "line": "/ Line", "rectangle": "▭ Rect",
    "circle": "○ Circle", "square": "□ Square", "right_triangle": "◺ R-Tri",
    "equil_triangle": "△ E-Tri", "rhombus": "◇ Rhombus", "eraser": "◻ Eraser",
    "fill": "🪣 Fill", "text": "T  Text",
}

def draw_button(surf, rect, label, active, font):
    color  = ACCENT if active else (60, 60, 80)
    border = WHITE  if active else (90, 90, 110)
    pygame.draw.rect(surf, color, rect, border_radius=6)
    pygame.draw.rect(surf, border, rect, 1, border_radius=6)
    txt = font.render(label, True, WHITE)
    surf.blit(txt, txt.get_rect(center=rect.center))

def draw_toolbar(surf, state, font_sm, font_xs):
    surf.fill(TOOLBAR_BG, (0, 0, TOOLBAR_W, SCREEN_H))
    pygame.draw.line(surf, (70, 70, 90), (TOOLBAR_W-1, 0), (TOOLBAR_W-1, SCREEN_H))

    t = font_sm.render("🎨 Paint", True, ACCENT)
    surf.blit(t, (10, 8))

    y = 40
    for tool in TOOLS:
        r = pygame.Rect(8, y, TOOLBAR_W-16, 26)
        draw_button(surf, r, TOOL_LABELS[tool], state["tool"] == tool, font_xs)
        state["tool_rects"][tool] = r
        y += 30
    
    y += 10
    lbl = font_xs.render("Size:", True, (180,180,180))
    surf.blit(lbl, (8, y)); y += 16
    for k, px in BRUSH_SIZES.items():
        r = pygame.Rect(8 + (k-1)*54, y, 50, 22)
        draw_button(surf, r, f"{k}", state["brush_key"] == k, font_xs)
        state["size_rects"][k] = r

    hint = font_xs.render("Ctrl+S = Save", True, (120,120,140))
    surf.blit(hint, (8, SCREEN_H - 22))

# НОВАЯ ФУНКЦИЯ ДЛЯ ЦЕНТРАЛЬНОЙ ПАЛИТРЫ
def draw_floating_palette(surf, state):
    # Размеры палитры
    rows, cols = 2, 6
    cell_w, cell_h = 35, 30
    gap = 5
    pal_w = cols * (cell_w + gap) + gap
    pal_h = rows * (cell_h + gap) + gap
    
    # Позиция: снизу по центру холста
    x = CANVAS_X + (CANVAS_W - pal_w) // 2
    y = SCREEN_H - pal_h - 20
    
    # Фон палитры
    bg_rect = pygame.Rect(x, y, pal_w, pal_h)
    pygame.draw.rect(surf, (40, 40, 50), bg_rect, border_radius=10)
    pygame.draw.rect(surf, (80, 80, 100), bg_rect, 2, border_radius=10)
    
    state["palette_rects"] = {} # Сбрасываем для новых координат
    for i, col in enumerate(PALETTE):
        r = i // cols
        c = i % cols
        rect = pygame.Rect(x + gap + c*(cell_w+gap), y + gap + r*(cell_h+gap), cell_w, cell_h)
        pygame.draw.rect(surf, col, rect, border_radius=4)
        if col == state["color"]:
            pygame.draw.rect(surf, WHITE, rect, 2, border_radius=4)
        state["palette_rects"][i] = rect

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption("TSIS 2 — Center Palette")

    font_sm = pygame.font.SysFont("Arial", 15, bold=True)
    font_xs = pygame.font.SysFont("Arial", 12)
    font_txt= pygame.font.SysFont("Arial", 22)  

    canvas = pygame.Surface((CANVAS_W, CANVAS_H))
    canvas.fill(CANVAS_DEFAULT_BG)

    state = {
        "tool": "pencil", "brush_key": 2, "color": WHITE,
        "tool_rects": {}, "size_rects": {}, "palette_rects": {},
    }

    drawing, prev_pos, drag_start, preview_surf = False, None, None, None
    text_active, text_pos, text_buf = False, None, ""
    clock = pygame.time.Clock()

    def canvas_pos(mx, my): return (mx - CANVAS_X, my)
    def brush_size(): return BRUSH_SIZES[state["brush_key"]]

    def commit_shape(tmp_canvas, start, end):
        t, col, sz = state["tool"], state["color"], brush_size()
        if   t == "line": draw_line(tmp_canvas, start, end, col, sz)
        elif t == "rectangle": draw_rectangle(tmp_canvas, start, end, col, sz)
        elif t == "circle": draw_circle(tmp_canvas, start, end, col, sz)
        elif t == "square": draw_square(tmp_canvas, start, end, col, sz)
        elif t == "right_triangle": draw_right_triangle(tmp_canvas, start, end, col, sz)
        elif t == "equil_triangle": draw_equilateral_triangle(tmp_canvas, start, end, col, sz)
        elif t == "rhombus": draw_rhombus(tmp_canvas, start, end, col, sz)

    SHAPE_TOOLS = {"line","rectangle","circle","square","right_triangle","equil_triangle","rhombus"}

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = event.pos
                
                # Клик по палитре (проверяем в первую очередь)
                hit_palette = False
                for i, r in state["palette_rects"].items():
                    if r.collidepoint(mx, my):
                        state["color"] = PALETTE[i]
                        hit_palette = True
                if hit_palette: continue

                # Клик по тулбару
                if mx < TOOLBAR_W:
                    for tool, r in state["tool_rects"].items():
                        if r.collidepoint(mx, my): state["tool"] = tool
                    for k, r in state["size_rects"].items():
                        if r.collidepoint(mx, my): state["brush_key"] = k
                else:
                    # Клик по холсту
                    cx, cy = canvas_pos(mx, my)
                    if state["tool"] == "fill": flood_fill(canvas, (cx, cy), state["color"])
                    elif state["tool"] == "text": 
                        text_active, text_pos, text_buf = True, (cx, cy), ""
                    elif state["tool"] in SHAPE_TOOLS:
                        drawing, drag_start, preview_surf = True, (cx, cy), canvas.copy()
                    else:
                        drawing, prev_pos = True, (cx, cy)
                        c = CANVAS_DEFAULT_BG if state["tool"] == "eraser" else state["color"]
                        draw_pencil(canvas, None, (cx, cy), c, brush_size())

            elif event.type == pygame.MOUSEBUTTONUP:
                if drawing and drag_start and state["tool"] in SHAPE_TOOLS:
                    commit_shape(canvas, drag_start, canvas_pos(*event.pos))
                drawing, prev_pos, drag_start, preview_surf = False, None, None, None

            elif event.type == pygame.MOUSEMOTION and drawing:
                mx, my = event.pos
                if mx >= TOOLBAR_W:
                    cx, cy = canvas_pos(mx, my)
                    if state["tool"] in ["pencil", "eraser"]:
                        c = CANVAS_DEFAULT_BG if state["tool"] == "eraser" else state["color"]
                        draw_pencil(canvas, prev_pos, (cx, cy), c, brush_size())
                        prev_pos = (cx, cy)
                    elif state["tool"] in SHAPE_TOOLS:
                        canvas.blit(preview_surf, (0,0))
                        commit_shape(canvas, drag_start, (cx, cy))

        # Отрисовка
        screen.fill(TOOLBAR_BG)
        screen.blit(canvas, (CANVAS_X, 0))
        
        draw_toolbar(screen, state, font_sm, font_xs)
        draw_floating_palette(screen, state) # Палитра рисуется поверх всего
        
        if text_active:
            screen.blit(font_txt.render(text_buf + "|", True, state["color"]), (CANVAS_X + text_pos[0], text_pos[1]))
            
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()