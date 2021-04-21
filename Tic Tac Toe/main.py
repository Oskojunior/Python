import pygame as pg
import numpy as np
import sys

pg.init()
WIDTH = 600
HEIGHT = 600
SCREEN_COLOR = (41, 36, 44)
LINE_COLOR = (233, 219, 243)
CIRCLE_COLOR = (242, 58, 174)
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
X_COLOR = (58, 125, 242)
X_WIDTH = 27
LINE_WIDTH = 10
BOARD_ROWS = 3
BOARD_COLUMNS = 3
player = 1
game_over = False
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Tic Tac Toe')
screen.fill(SCREEN_COLOR)

board = np.zeros((BOARD_ROWS, BOARD_COLUMNS))

def draw_lines():
    pg.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    pg.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)
    pg.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    pg.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLUMNS):
            if board[row][col] == 1:
                pg.draw.circle(screen, CIRCLE_COLOR, (int(col * 200 + 200 / 2), int(row * 200 + 200 / 2)),
                               CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pg.draw.line(screen, X_COLOR, (col * 200 + 55, row * 200 + 200 - 55),
                             (col * 200 + 200 - 55, row * 200 + 55), X_WIDTH)
                pg.draw.line(screen, X_COLOR, (col * 200 + 55, row * 200 + 55),
                             (col * 200 + 200 - 55, row * 200 + 200 - 55), X_WIDTH)
def mark_square(row, col, player):
    board[row][col] = player

def square_available(row, col):
    return board[row, col] == 0

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLUMNS):
            if board[row][col] == 0:
                return False
    return True

def check_win(player):
	# vertical win check
	for col in range(BOARD_COLUMNS):
		if board[0][col] == player and board[1][col] == player and board[2][col] == player:
			draw_vertical_winning_line(col, player)
			return True

	# horizontal win check
	for row in range(BOARD_ROWS):
		if board[row][0] == player and board[row][1] == player and board[row][2] == player:
			draw_horizontal_winning_line(row, player)
			return True

	# asc diagonal win check
	if board[2][0] == player and board[1][1] == player and board[0][2] == player:
		draw_asc_diagonal(player)
		return True

	# desc diagonal win chek
	if board[0][0] == player and board[1][1] == player and board[2][2] == player:
		draw_desc_diagonal(player)
		return True

	return False

def draw_vertical_winning_line(col, player):
	posX = col * 200 + 200//2

	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = X_COLOR

	pg.draw.line( screen, color, (posX, 15), (posX, HEIGHT - 15), LINE_WIDTH )

def draw_horizontal_winning_line(row, player):
	posY = row * 200 + 200//2

	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = X_COLOR

	pg.draw.line( screen, color, (15, posY), (WIDTH - 15, posY), LINE_WIDTH )

def draw_asc_diagonal(player):
	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = X_COLOR

	pg.draw.line( screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), LINE_WIDTH )

def draw_desc_diagonal(player):
	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = X_COLOR

	pg.draw.line( screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), LINE_WIDTH )

def restart():
	screen.fill( SCREEN_COLOR )
	draw_lines()
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COLUMNS):
			board[row][col] = 0

draw_lines()


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)
            if square_available(clicked_row, clicked_col):
                if player == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    if check_win(player):
                        game_over = True
                    player = 2
                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    if check_win(player):
                        game_over = True
                    player = 1
                draw_figures()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_r:
                restart()
                player = 1
                game_over = False
    pg.display.update()
