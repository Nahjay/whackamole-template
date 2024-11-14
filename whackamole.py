import pygame
import random


def main():
    try:
        # Init pygame object
        pygame.init()

        # Create mole image, screen, and clock
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()

        # State tracker
        running = True

        # Color tuple
        black = (0, 0, 0)

        # Init position
        x, y = 0, 0

        # Mole pos object
        mole_rect = mole_image.get_rect(topleft=(x, y))

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                # Mouse Click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Get mouse pos
                    mouse_pos = pygame.mouse.get_pos()

                    # Check for collision
                    if mole_rect.collidepoint(mouse_pos):
                        # Generate random pos
                        x = random.randrange(0, 640, 32)
                        y = random.randrange(0, 512, 32)

                        # Draw Mole Again
                        mole_rect.topleft = (x, y)

            screen.fill("light green")
            # Draw Lines
            for i in range(0, 640, 32):
                pygame.draw.line(screen, black, (i, 0), (i, 512), 1)
            for i in range(0, 512, 32):
                pygame.draw.line(screen, black, (0, i), (640, i), 1)

            # Draw Mole
            screen.blit(mole_image, mole_rect)
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
