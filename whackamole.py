import pygame
import random
#20 by 16 grid


def main():
    try:
        #test
        x = random.randrange(1, 17)
        y = random.randrange(1, 21)

        pygame.init()
        screen = pygame.display.set_mode((640, 512))

        def draw_grid():
            i = 1
            while i < 20:
                pygame.draw.line(screen, "black", (i * 32, 0), (i * 32, 512))
                pygame.draw.line(screen, "black", (0, i * 32), (640, i * 32))
                i = i + 1

        mole_image = pygame.image.load("mole.png")

        screen = pygame.display.set_mode((640, 512))

        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    #for clicky
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)
                    correct_column = False
                    correct_row = False
                    for i in event.pos:
                        if correct_column == False:
                            if (i//32 == x):
                                print("correct column")
                                correct_column = True
                                pass
                        if correct_column == True:
                            if (i//32 == y):
                                print("correct row")
                                correct_row = True
                    if correct_row == True and correct_column == True:
                        print("correct row and column")
                        x = random.randrange(1, 17)
                        y = random.randrange(1, 21)
                        draw_grid()
                        screen.blit(mole_image, mole_image.get_rect(topleft=(x * 32, y * 32)))
            screen.fill("light green")
            screen.blit(mole_image, mole_image.get_rect(topleft=(x * 32, y * 32)))
            draw_grid()



            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
