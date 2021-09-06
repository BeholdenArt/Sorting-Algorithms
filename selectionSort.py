import pygame
import base
import sys

def main():
    fps = 60
    screen = pygame.display.set_mode(base.win_size)
    algo = "Selection Sort"
    bar_height, bar_color = base.generate_bars()

    counter = 0
    while True:
        screen.fill(base.BLACK)
        base.draw_everything(screen, algo, fps)

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
                        bar_color[j] = base.RED
                        base.draw_everything(screen, algo, fps)
                    bar_color[minimum] = base.WHITE

                bar_height[minimum], bar_height[counter] = bar_height[counter], bar_height[minimum]
                bar_color[counter] = base.GREEN
                counter += 1

            else:
                base.draw_everything(screen, algo, fps)
        elif pressed[pygame.K_q]:
            fps = 60
        elif pressed[pygame.K_w]:
            fps = 30
        elif pressed[pygame.K_e]:
            fps = 10


if __name__ == "__main__":
    main()
