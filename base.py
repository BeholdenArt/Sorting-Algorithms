import pygame
import random
pygame.init()

BLACK = pygame.Color("Black")
WHITE = pygame.Color("White")
RED = pygame.Color("Red")
GREEN = pygame.Color("Green")
PINK = pygame.Color("Pink")

win_size = (WIDTH, HEIGHT) = 900, 700
screen = pygame.display.set_mode(win_size)
pygame.display.set_caption("SORTING ALGORITHM VISUALIZER")
clock = pygame.time.Clock()

bar_height = []
bar_color = []
n = 35
bar_width = 31


def generate_bars():
    for i in range(WIDTH//n):
        bar_height.append(random.randint(100, HEIGHT-150))
        bar_color.append(WHITE)
    return bar_height, bar_color


def draw_text(algorithm, fps):
    heading_text = pygame.font.SysFont("Consolas", 40).render(algorithm, True, WHITE)
    heading_box = heading_text.get_rect(center=(WIDTH // 2, 30))
    info_text = pygame.font.SysFont("Consolas", 20).render("(Press Space)", True, WHITE)
    info_box = info_text.get_rect(center=(WIDTH // 2, 60))
    fps_info = pygame.font.SysFont("Consolas", 15).render("(Q: 60, W: 30, E: 10)", True, WHITE)
    fps_info_box = (15, 50)
    fps_text = pygame.font.SysFont("Consolas", 20).render("FPS: "+str(fps), True, WHITE)
    fps_box = (50, 30)
    return [[heading_text, heading_box], [info_text, info_box],
            [fps_text, fps_box], [fps_info, fps_info_box]]


def draw_everything(scr, algo, fps):
    clock.tick(fps)
    text = draw_text(algorithm=algo, fps= fps)
    scr.blit(text[0][0], text[0][1])
    scr.blit(text[1][0], text[1][1])
    scr.blit(text[2][0], text[2][1])
    scr.blit(text[3][0], text[3][1])
    pygame.draw.line(scr, WHITE, (0, 80), (WIDTH, 80), 10)
    for var in range(WIDTH // n):
        pygame.draw.rect(scr, bar_color[var],
                         pygame.Rect(((var * 5) + (var * bar_width)), 90, bar_width, bar_height[var]))

    pygame.display.update()
