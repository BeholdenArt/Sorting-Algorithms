import sys
import random
import pygame
pygame.init()

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

win_size = (WIDTH, HEIGHT) = 800, 600
screen = pygame.display.set_mode(win_size)
pygame.display.set_caption("Quick Sort v2.0")
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

    for var in range(WIDTH//n):
        pygame.draw.rect(screen, bar_color[var], pygame.Rect(((var*5)+(var*bar_width)), 90, bar_width, bar_height[var]))
    pygame.display.flip()


def partition(arr, beg, stop):
    var = beg
    pivot = arr[stop]

    for j in range(beg, stop):
        if arr[j] < pivot:
            arr[var], arr[j] = arr[j], arr[var]
            var += 1
    arr[var], arr[stop] = arr[stop], arr[var]
    return var


def main():
    end = len(bar_height) - 1
    start = 0
    size = end - start + 1
    stack = [0] * size

    top = 0
    stack[top] = 0
    top += 1
    stack[top] = end

    counter = 0
    while True:
        screen.fill(BLACK)
        draw_everything()

        if top < 0:
            if counter < len(bar_height):
                bar_color[counter] = GREEN
                counter += 1
        else:
            end = stack[top]
            top -= 1
            start = stack[top]
            top -= 1

            p = partition(bar_height, start, end)
            bar_color[p] = RED

            if p-1 > start:
                top += 1
                stack[top] = start
                top += 1
                stack[top] = p-1
            if p+1 < end:
                top += 1
                stack[top] = p+1
                top += 1
                stack[top] = end

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    main()
