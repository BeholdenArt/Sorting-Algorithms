import random
import sys
import pygame
pygame.init()

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

win_size = (WIDTH, HEIGHT) = 900, 700
screen = pygame.display.set_mode(win_size)
pygame.display.set_caption("Bubble Sort v1.1")
clock = pygame.time.Clock()

bar_height = []
bar_color = []
n = 35
bar_width = 31

HEADING_TEXT = pygame.font.SysFont("Consolas", 40).render("SELECTION SORT", True, WHITE)
HEADING_BOX = HEADING_TEXT.get_rect(center=(WIDTH//2, 30))
INFO_TEXT = pygame.font.SysFont("Consolas", 20).render("(Press Space)", True, WHITE)
INFO_BOX = INFO_TEXT.get_rect(center=(WIDTH//2, 60))

for i in range(WIDTH // n):
    bar_height.append(random.randint(100, HEIGHT-150))
    bar_color.append(WHITE)


def draw_everything():
    clock.tick(10)
    screen.blit(HEADING_TEXT, HEADING_BOX)
    screen.blit(INFO_TEXT, INFO_BOX)
    pygame.draw.line(screen, WHITE, (0, 80), (WIDTH, 80), 10)
    for var in range(WIDTH // n):
        pygame.draw.rect(screen, bar_color[var], pygame.Rect(((var*5)+(var*bar_width)), 90, bar_width, bar_height[var]))
    pygame.display.flip()


def main():
    counter = 0
    while True:
        screen.fill(BLACK)
        draw_everything()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            if counter < len(bar_height):
                minimum = counter
                for j in range(counter + 1, len(bar_height)):
                    if bar_height[minimum] > bar_height[j]:
                        minimum = j
                        bar_color[j] = RED
                        draw_everything()
                    bar_color[minimum] = WHITE

                bar_height[minimum], bar_height[counter] = bar_height[counter], bar_height[minimum]
                bar_color[counter] = GREEN
                counter += 1

            else:
                draw_everything()


if __name__ == "__main__":
    main()
