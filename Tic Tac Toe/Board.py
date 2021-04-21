import pygame as pg
import numpy as np
import Player

class Board:
    def __init__(self, width, height, screen_color, line_color, line_width):
        pg.init()
        self.WIDTH = width
        self.HEIGHT = height
        self.SCREEN_COLOR = screen_color
        self.LINE_COLOR = line_color
        self.LINE_WIDTH = line_width
        self.BOARD_ROWS = 3
        self.BOARD_COLUMNS = 3
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        self.screen.fill(self.SCREEN_COLOR)
        self.board = np.zeros((self.BOARD_ROWS, self.BOARD_COLUMNS))
        self.player_O = Player.Circle(15, (242, 58, 174), 60)
        self.player_X = Player.X(27, (58, 125, 242))
        self.game_over = False
        self.draw_lines()

    def draw_lines(self):
        pg.draw.line(self.screen, self.LINE_COLOR, (0, 200), (600, 200), self.LINE_WIDTH)
        pg.draw.line(self.screen, self.LINE_COLOR, (0, 400), (600, 400), self.LINE_WIDTH)
        pg.draw.line(self.screen, self.LINE_COLOR, (200, 0), (200, 600), self.LINE_WIDTH)
        pg.draw.line(self.screen, self.LINE_COLOR, (400, 0), (400, 600), self.LINE_WIDTH)

    def draw_figures(self):
        for row in range(self.BOARD_ROWS):
            for col in range(self.BOARD_COLUMNS):
                if self.board[row][col] == 1:
                    self.player_O.draw_circle(self.screen, col, row)
                elif self.board[row][col] == -1:
                    self.player_X.draw_x(self.screen, col, row)

    def draw_vertical_winning_line(self, col, player):
        posX = col * 200 + 100

        if player == 1:
            color = self.player_O.color
        elif player == -1:
            color = self.player_X.color

        pg.draw.line(self.screen, color, (posX, 15), (posX, self.HEIGHT - 15), self.LINE_WIDTH)

    def draw_horizontal_winning_line(self, row, player):
        posY = row * 200 + 200 // 2

        if player == 1:
            color = self.player_O.color
        elif player == -1:
            color = self.player_X.color

        pg.draw.line(self.screen, color, (15, posY), (self.WIDTH - 15, posY), self.LINE_WIDTH)

    def draw_asc_diagonal(self, player):
        if player == 1:
            color = self.player_O.color
        elif player == -1:
            color = self.player_X.color

        pg.draw.line(self.screen, color, (15, self.HEIGHT - 15), (self.WIDTH - 15, 15), self.LINE_WIDTH)

    def draw_desc_diagonal(self, player):
        if player == 1:
            color = self.player_O.color
        elif player == -1:
            color = self.player_X.color

        pg.draw.line(self.screen, color, (15, 15), (self.WIDTH - 15, self.HEIGHT - 15), self.LINE_WIDTH)

    def mark_square(self, row, col, player):
        self.board[row][col] = player

    def square_available(self, row, col):
        return self.board[row, col] == 0

    def is_board_full(self):
        for row in range(self.BOARD_ROWS):
            for col in range(self.BOARD_COLUMNS):
                if self.board[row][col] == 0:
                    return False
        return True

    def check_win(self, player):
        # vertical win check
        for col in range(self.BOARD_COLUMNS):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] == player:
                self.draw_vertical_winning_line(col, player)
                return True

    # horizontal win check
        for row in range(self.BOARD_ROWS):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] == player:
                self.draw_horizontal_winning_line(row, player)
                return True

    # asc diagonal win check
        if self.board[2][0] == self.board[1][1] == self.board[0][2] == player:
            self.draw_asc_diagonal(player)
            return True

    # desc diagonal win chek
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            self.draw_desc_diagonal(player)
            return True

        return False

    def restart(self):
        self.screen.fill(self.SCREEN_COLOR)
        self.draw_lines()
        for row in range(self.BOARD_ROWS):
            for col in range(self.BOARD_COLUMNS):
                self.board[row][col] = 0
