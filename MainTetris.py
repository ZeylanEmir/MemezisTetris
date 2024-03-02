import pygame
import sys
from game import Game
from colors import Colors
from button import Button
pygame.init()

def play():
    pygame.init()

    title_font = pygame.font.Font(None, 40)
    score_surface = title_font.render("Score", True, Colors.white)
    next_surface = title_font.render("Next", True, Colors.white)
    game_over_surface = title_font.render("GAME OVER", True, Colors.white)


    score_rect = pygame.Rect(320, 55, 170, 60)
    next_rect = pygame.Rect(320, 215, 170, 180)

    screen = pygame.display.set_mode((500, 620))
    pygame.display.set_caption("Memezis Tetris")

    clock = pygame.time.Clock()

    game = Game()

    GAME_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(GAME_UPDATE, 200)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if game.game_over == True:
                    game.game_over = False
                    game.reset()
                if event.key == pygame.K_LEFT and game.game_over == False:
                    game.move_left()
                if event.key == pygame.K_RIGHT and game.game_over == False:
                    game.move_right()
                if event.key == pygame.K_DOWN and game.game_over == False:
                    game.move_down()
                    game.update_score(0, 1)
                if event.key == pygame.K_UP and game.game_over == False:
                    game.rotate()

            if event.type == GAME_UPDATE and game.game_over == False:
                game.move_down()

        # Drawning
        score_value_surface = title_font.render(str(game.score), True, Colors.white)

        screen.fill(Colors.dark_blue)
        screen.blit(score_surface, (365, 20, 50, 50))
        screen.blit(next_surface, (375, 180, 50, 50))

        if game.game_over == True:
            screen.blit(game_over_surface, (320, 450, 50, 50))

        pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
        screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx,
                                                                      centery = score_rect.centery))
        pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
        game.draw(screen)

        pygame.display.update()
        clock.tick(60)



SCREEN = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)






def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(250, 60))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(250, 200),
                             text_input="PLAY", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(250, 400),
                             text_input="QUIT", font=get_font(50), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()