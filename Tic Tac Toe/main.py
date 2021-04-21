import pygame as pg
import Board
import sys

board = Board.Board()
on_move = 1

def turn(on_move):
    return on_move * -1


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN and not board.game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            if mouseY < 601:
                clicked_row = int(mouseY // 200)
                clicked_col = int(mouseX // 200)
                if board.square_available(clicked_row, clicked_col):
                    board.mark_square(clicked_row, clicked_col, on_move)
                    if board.check_win(on_move):
                        board.game_over = True
                    on_move = turn(on_move)
                    board.draw_figures()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_r:
                board.restart()
                on_move = 1
                board.game_over = False
        pg.display.update()
