import pygame
import random

def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        moleScreenPos= (0,0)        # Position of the mole image on the screen
        moleGridPos = (0,0)         # Position of the mole image on the grid
        screen = pygame.display.set_mode((640, 512))
        pygame.display.set_caption("Whackamole")
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    col, row = x//32, y//32
                    if (col,row) == moleGridPos:
                        newCol= random.randrange(0,608)//32
                        newRow= random.randrange(0,480)//32
                        moleGridPos = (newCol,newRow)           # Sets new grid position for next check
                        moleScreenPos = (newCol*32,newRow*32)   # Sets new screen position for screen.blit()
            screen.fill("light green")
            for i in range(1, 16):
                pygame.draw.line(screen, 000000, (0, i * 32), (640, i * 32), 1)
            for i in range(1, 20):
                pygame.draw.line(screen, 000000, (i * 32, 0), (i * 32, 512), 1)
            screen.blit(mole_image, mole_image.get_rect(topleft=moleScreenPos))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()