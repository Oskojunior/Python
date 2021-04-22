import pygame as pg
import pygame.freetype
import numpy as np
import Player
import AI
class Board:
    def __init__(self):
        pg.init()
        self.WIDTH = 600
        self.HEIGHT = 700
        self.SCREEN_COLOR = (41, 36, 44)
        self.LINE_COLOR = (233, 219, 243)
        self.LINE_WIDTH = 10
        self.BOARD_ROWS = 3
        self.BOARD_COLUMNS = 3
        self.SCORE_BOARD_PLACE = (220, 650)
        self.FONT = pg.freetype.Font('Pacifico.ttf', 36)
        self.FONT_COLOR = (250, 244, 74)
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        self.screen.fill(self.SCREEN_COLOR)
        self.board = np.zeros((self.BOARD_ROWS, self.BOARD_COLUMNS))
        self.player_O = Player.Circle(15, (242, 58, 174), 60)
        self.player_X = Player.X(27, (58, 125, 242))
        self.game_over = False
        self.draw_lines()
        self.FONT.render_to(self.screen, self.SCORE_BOARD_PLACE, "Score: " + str(self.player_O.score) + " : " +
                            str(self.player_X.score), self.FONT_COLOR)

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

        pg.draw.line(self.screen, color, (posX, 15), (posX, 600), self.LINE_WIDTH)

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

        pg.draw.line(self.screen, color, (15, 585), (self.WIDTH - 15, 15), self.LINE_WIDTH)

    def draw_desc_diagonal(self, player):
        if player == 1:
            color = self.player_O.color
        elif player == -1:
            color = self.player_X.color

        pg.draw.line(self.screen, color, (15, 15), (self.WIDTH - 15, 585), self.LINE_WIDTH)

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
                self.add_point(player)
                return True

        # horizontal win check
        for row in range(self.BOARD_ROWS):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] == player:
                self.draw_horizontal_winning_line(row, player)
                self.add_point(player)
                return True

        # asc diagonal win check
        if self.board[2][0] == self.board[1][1] == self.board[0][2] == player:
            self.draw_asc_diagonal(player)
            self.add_point(player)
            return True

        # desc diagonal win chek
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            self.draw_desc_diagonal(player)
            self.add_point(player)
            return True

        return False

    def add_point(self, player):
        if player == 1:
            self.player_O.score += 1
        else:
            self.player_X.score += 1

    def restart(self):
        self.screen.fill(self.SCREEN_COLOR)
        self.draw_lines()
        self.FONT.render_to(self.screen, self.SCORE_BOARD_PLACE, "Score: " + str(self.player_O.score) + " : " +
                            str(self.player_X.score), self.FONT_COLOR)
        for row in range(self.BOARD_ROWS):
            for col in range(self.BOARD_COLUMNS):
                self.board[row][col] = 0
