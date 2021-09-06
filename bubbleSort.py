import sys
import base
import pygame

def main():
    fps = 60
    screen = pygame.display.set_mode(base.win_size)
    bar_height, bar_color = base.generate_bars()
    algo = "Bubble Sort"

    counter = 0
    while True:
        screen.fill(base.BLACK)
        base.draw_everything(screen, algo, fps)
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            if counter < len(bar_height):
                for j in range(0, len(bar_height) - counter - 1):
                    if bar_height[j] < bar_height[j + 1]:
                        bar_color[j] = bar_color[j + 1] = base.RED
                        base.draw_everything(screen, algo, fps)
                        bar_height[j], bar_height[j + 1] = bar_height[j + 1], bar_height[j]
                        bar_color[j] = bar_color[j + 1] = base.WHITE
                bar_color[len(bar_height) - counter - 1] = base.GREEN
                counter += 1
        elif pressed[pygame.K_q]:
            fps = 60
        elif pressed[pygame.K_w]:
            fps = 30
        elif pressed[pygame.K_e]:
            fps = 10
        else:
            base.draw_everything(screen, algo, fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



if __name__ == "__main__":
    main()
