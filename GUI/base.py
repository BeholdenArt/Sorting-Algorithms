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
pygame.display.set_caption("Insertion Sort v2.0")
clock = pygame.time.Clock()

bar_height = []
bar_color = []
n = 35
bar_width = 31

ALGORITHM = ""

def generate_bars():
    for i in range(WIDTH//n):
        bar_height.append(random.randint(100, HEIGHT-150))
        bar_color.append(WHITE)
    return bar_height, bar_color

def setting_algorithm(algorithm_name):
    global ALGORITHM
    ALGORITHM = algorithm_name

def draw_text(algorithm):
    HEADING_TEXT = pygame.font.SysFont("Consolas", 40).render(algorithm, True, WHITE)
    HEADING_BOX = HEADING_TEXT.get_rect(center=(WIDTH // 2, 30))
    INFO_TEXT = pygame.font.SysFont("Consolas", 20).render("(Press Space)", True, WHITE)
    INFO_BOX = INFO_TEXT.get_rect(center=(WIDTH // 2, 60))
    screen.blit(HEADING_TEXT, HEADING_BOX)
    screen.blit(INFO_TEXT, INFO_BOX)

def draw_everything(algo):
    clock.tick(10)
    draw_text(algorithm= algo)
    pygame.draw.line(screen, WHITE, (0, 80), (WIDTH, 80), 10)
    for var in range(WIDTH // n):
        pygame.draw.rect(screen, bar_color[var],
                         pygame.Rect(((var * 5) + (var * bar_width)), 90, bar_width, bar_height[var]))

    pygame.display.update()
