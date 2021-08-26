import sys
import random
import pygame

pygame.init()

win_size = (WIDTH, HEIGHT) = 800, 600
screen = pygame.display.set_mode(win_size)
pygame.display.set_caption("QUICK SORT")
clock = pygame.time.Clock()

n = 10
h_arr = []
state = []

for i in range(WIDTH // n):
    h_arr.append(random.randint(10, HEIGHT - 50))
    state.append(1)


def partition(arr, beg, stop):
    for var in range(beg, stop):
        state[var] = 0
    var = beg
    pivot = arr[stop]
    state[beg] = 0

    for j in range(beg, stop):
        if arr[j] < pivot:
            arr[var], arr[j] = arr[j], arr[var]
            state[var] += 1
            var += 1
            state[var] = 0

    arr[var], arr[stop] = arr[stop], arr[var]
    return var


end = len(h_arr) - 1
start = 0
size = end - start + 1
stack = [0] * size

top = 0
stack[top] = 0
top += 1
stack[top] = end

counter = 0
heading_text = pygame.font.SysFont('Consolas', 40).render("QUICK SORT", True, pygame.color.Color('White'))
heading_text_rect = heading_text.get_rect(center=(WIDTH // 2, 20))
done_text = pygame.font.SysFont('Consolas', 32).render('Sorting Complete.', True, pygame.color.Color('White'))
done_text_rect = (100, 100)

while True:
    screen.fill(pygame.Color("black"))
    clock.tick(20)
    screen.blit(heading_text, heading_text_rect)
    if top < 0:
        if counter < len(h_arr):
            state[counter] = 2
            counter += 1
            screen.blit(done_text, done_text_rect)

    else:
        end = stack[top]
        top -= 1
        start = stack[top]
        top -= 1

        p = partition(h_arr, start, end)

        state[p] = 1
        if p - 1 > start:
            top += 1
            stack[top] = start
            top += 1
            stack[top] = p - 1

        if p + 1 < end:
            top += 1
            stack[top] = p + 1
            top += 1
            stack[top] = end

    for i in range(len(h_arr)):
        if state[i] == 0:
            color = pygame.Color("Red")
        elif state[i] == 2:
            color = pygame.Color("Green")
        else:
            color = pygame.Color("Grey")

        pygame.draw.rect(screen, color, pygame.Rect(i * n, HEIGHT - h_arr[i], n, h_arr[i]))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
