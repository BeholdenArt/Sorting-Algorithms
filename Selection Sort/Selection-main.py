import random
import sys
import pygame
pygame.init()

win_size = (WIDTH, HEIGHT) = 900, 700

screen = pygame.display.set_mode(win_size)
pygame.display.set_caption("Selection Sort")
clock = pygame.time.Clock()

n = 15

h_arr = []
color = []

for i in range(WIDTH//n):
    height = random.randint(10, HEIGHT-50)
    h_arr.append(height)
    color.append([random.randint(0, 200), random.randint(0, 200), random.randint(0, 200)])

counter = 0
minimum = 0

heading_text = pygame.font.SysFont('Consolas', 40).render("SELECTION SORT", True, pygame.color.Color('White'))
heading_text_rect = heading_text.get_rect(center=(WIDTH//2, 20))
done_text = pygame.font.SysFont('Consolas', 32).render('Sorting Complete.', True, pygame.color.Color('White'))
done_text_rect = (100, 100)

while True:
    screen.fill(pygame.color.Color('Black'))
    clock.tick(10)
    screen.blit(heading_text, heading_text_rect)
    if counter < (len(h_arr)):
        minimum = counter

        for j in range(counter+1, len(h_arr)):
            if h_arr[minimum] > h_arr[j]:
                minimum = j
        h_arr[minimum], h_arr[counter] = h_arr[counter], h_arr[minimum]
    else:
        screen.blit(done_text, done_text_rect)

    for i in range(len(h_arr)):
        pygame.draw.rect(screen, color[i], pygame.Rect(int(i*n), HEIGHT - h_arr[i], n, h_arr[i]))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    counter += 1
