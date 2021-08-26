import sys
import random
import pygame

pygame.init()

win_size = (WIDTH, HEIGHT) = 800, 600
screen = pygame.display.set_mode(win_size)
pygame.display.set_caption("INSERTION SORT")
clock = pygame.time.Clock()

n = 10

h_arr = []
colors = []
for i in range(WIDTH // n):
    h_arr.append(random.randint(10, HEIGHT - 100))
    colors.append([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])

counter = 0
j = 0

heading_text = pygame.font.SysFont('Consolas', 40).render("INSERTION SORT", True, pygame.color.Color('White'))
heading_text_rect = heading_text.get_rect(center=(WIDTH//2, 20))
done_text = pygame.font.SysFont('Consolas', 32).render('Sorting Complete.', True, pygame.color.Color('White'))
done_text_rect = (100, 100)

while True:
    screen.fill(pygame.color.Color("Black"))
    clock.tick(10)
    screen.blit(heading_text, heading_text_rect)

    if counter < len(h_arr):
        key = h_arr[counter]
        j = counter - 1

        while j >= 0 and key < h_arr[j]:
            h_arr[j + 1] = h_arr[j]
            j -= 1
        h_arr[j + 1] = key
    else:
        screen.blit(done_text, done_text_rect)
    counter += 1

    for i in range(len(h_arr)):
        pygame.draw.rect(screen, colors[i], (i * n, HEIGHT - h_arr[i], n, h_arr[i]))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
