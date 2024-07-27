import pygame
import sys
from game import Game as TetrisGame
from colors import Colors as Palette

pygame.init()

# Fonts and Text Surfaces
header_font = pygame.font.Font(None, 40)
score_label = header_font.render("Score", True, Palette.white)
next_label = header_font.render("Next", True, Palette.white)
game_over_label = header_font.render("GAME OVER", True, Palette.white)

# Rectangles for UI Elements
score_box = pygame.Rect(320, 55, 170, 60)
upcoming_box = pygame.Rect(320, 215, 170, 180)

# Main Window
main_screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Tetris Clone")

# Frame Rate Control
frame_rate = pygame.time.Clock()

# Initialize Game Instance
tetris_instance = TetrisGame()

# Custom Event for Game Update
UPDATE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(UPDATE_EVENT, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if tetris_instance.is_game_over:
                tetris_instance.is_game_over = False
                tetris_instance.reset_game()
            if event.key == pygame.K_LEFT and not tetris_instance.is_game_over:
                tetris_instance.move_piece_left()
            if event.key == pygame.K_RIGHT and not tetris_instance.is_game_over:
                tetris_instance.move_piece_right()
            if event.key == pygame.K_DOWN and not tetris_instance.is_game_over:
                tetris_instance.drop_piece()
                tetris_instance.increment_score(0, 1)
            if event.key == pygame.K_UP and not tetris_instance.is_game_over:
                tetris_instance.rotate_piece()
        if event.type == UPDATE_EVENT and not tetris_instance.is_game_over:
            tetris_instance.drop_piece()

    # Rendering
    score_value_label = header_font.render(str(tetris_instance.score), True, Palette.white)

    main_screen.fill(Palette.dark_blue)
    main_screen.blit(score_label, (365, 20, 50, 50))
    main_screen.blit(next_label, (375, 180, 50, 50))

    if tetris_instance.is_game_over:
        main_screen.blit(game_over_label, (320, 450, 50, 50))

    pygame.draw.rect(main_screen, Palette.light_blue, score_box, 0, 10)
    main_screen.blit(score_value_label, score_value_label.get_rect(centerx=score_box.centerx, centery=score_box.centery))
    pygame.draw.rect(main_screen, Palette.light_blue, upcoming_box, 0, 10)
    tetris_instance.render(main_screen)

    pygame.display.update()
    frame_rate.tick(60)
