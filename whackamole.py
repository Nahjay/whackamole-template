import pygame
import random


def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        black = (0, 0, 0)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light green")
            # Draw Lines
            for i in range(0, 640, 32):
                pygame.draw.line(screen, black, (i, 0), (i, 512), 1)
            for i in range(0, 512, 32):
                pygame.draw.line(screen, black, (0, i), (640, i), 1)

            # Draw Mole
            screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
