import random
import sys
import pygame
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

HEADING_TEXT = pygame.font.SysFont("Consolas", 40).render("INSERTION SORT", True, WHITE)
HEADING_BOX = HEADING_TEXT.get_rect(center=(WIDTH // 2, 30))
INFO_TEXT = pygame.font.SysFont("Consolas", 20).render("(Press Space)", True, WHITE)
INFO_BOX = INFO_TEXT.get_rect(center=(WIDTH // 2, 60))

for i in range(WIDTH//n):
    bar_height.append(random.randint(100, HEIGHT-150))
    bar_color.append(WHITE)


def draw_everything():
    clock.tick(10)
    screen.blit(HEADING_TEXT, HEADING_BOX)
    screen.blit(INFO_TEXT, INFO_BOX)
    pygame.draw.line(screen, WHITE, (0, 80), (WIDTH, 80), 10)
    for var in range(WIDTH // n):
        pygame.draw.rect(screen, bar_color[var],
                         pygame.Rect(((var * 5) + (var * bar_width)), 90, bar_width, bar_height[var]))

    pygame.display.update()


def main():
    counter = 1

    while True:
        screen.fill(BLACK)
        draw_everything()

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            if counter < len(bar_height):
                key = bar_height[counter]
                j = counter - 1
                while j >= 0 and key < bar_height[j]:
                    bar_color[j+1] = bar_color[j] = GREEN
                    bar_height[j+1] = bar_height[j]
                    j -= 1
                bar_height[j+1] = key
                bar_color[counter] = RED
                counter += 1

            else:
                bar_color[counter-1] = GREEN
                draw_everything()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()
