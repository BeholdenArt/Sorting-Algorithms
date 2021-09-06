import sys
import pygame
import base


def main():
    fps = 60
    screen = pygame.display.set_mode(base.win_size)

    bar_height, bar_color = base.generate_bars()
    algo = "Insertion Sort"

    counter = 1
    while True:
        base.screen.fill(base.BLACK)
        base.draw_everything(screen, algo, fps)

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            if counter < len(bar_height):
                key = bar_height[counter]
                j = counter - 1
                while j >= 0 and key < bar_height[j]:
                    bar_color[j+1] = bar_color[j] = base.GREEN
                    bar_height[j+1] = bar_height[j]
                    j -= 1
                bar_height[j+1] = key
                bar_color[counter] = base.RED
                counter += 1
            else:
                bar_color[counter-1] = base.GREEN
                base.draw_everything(screen, algo, fps)
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



if __name__ == "__main__":
    main()
