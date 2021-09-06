import base
import pygame
import sys

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
    screen = pygame.display.set_mode(base.win_size)
    fps = 60
    algo = "Quick Sort"
    bar_height, bar_color = base.generate_bars()

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
        screen.fill(base.BLACK)
        base.draw_everything(screen, algo, fps)

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            if top < 0:
                if counter < len(bar_height):
                    base.bar_color[counter] = base.GREEN
                    counter += 1
            else:
                end = stack[top]
                top -= 1
                start = stack[top]
                top -= 1

                p = partition(bar_height, start, end)
                base.bar_color[p] = base.RED

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
        elif pressed[pygame.K_q]:
            fps = 60
        elif pressed[pygame.K_w]:
            fps = 30
        elif pressed[pygame.K_e]:
            fps = 10

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    main()
