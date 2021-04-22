import pyautogui as mouse
import copy
import random
import time

class AI:

    def move(self, board):
        possible_moves = self.possible_moves(board)
        for win in [-1, 1]:
            for i in possible_moves:
                board_copy = copy.copy(board)
                board_copy[i[0]][i[1]] = win
                if self.check_win(board_copy, win):
                    mouse.moveTo(1920/2 + i[1] * 200 - 150, 1080/2 + i[0] * 200 - 200, 0.5)
                    time.sleep(0.1)
                    mouse.leftClick()
                    return

        cornersOpen = []
        for i in possible_moves:
            if i in [(0, 0), (2, 0), (0, 2), (2, 2)]:
                cornersOpen.append(i)
        if len(cornersOpen) > 0:
            move = random.choice(cornersOpen)
            mouse.moveTo(1920/2 + move[1] * 200 - 150, 1080/2 + move[0] * 200 - 200, 0.5)
            time.sleep(0.5)
            mouse.leftClick()
            return

        if (1, 1) in possible_moves:
            mouse.moveTo(1920 / 2 + 1 * 200 - 150, 1080 / 2 + 1 * 200 - 200, 0.5)
            time.sleep(0.5)
            mouse.leftClick()
            return

        edgesOpen = []
        for i in possible_moves:
            if i in [(1, 0), (0, 1), (1, 2), (2, 1)]:
                edgesOpen.append(i)
        if len(edgesOpen) > 0:
            move = random.choice(edgesOpen)
            mouse.moveTo(1920 / 2 + move[1] * 200 - 150, 1080 / 2 + move[0] * 200 - 200, 0.5)
            time.sleep(0.5)
            mouse.leftClick()
            return

    def possible_moves(self, board):
        possible_moves = []
        for col in range(3):
            for row in range(3):
                if board[row][col] == 0:
                    possible_moves.append((row, col))
        return possible_moves

    def check_win(self, board_copy, win):

        for col in range(3):
            if board_copy[0][col] == board_copy[1][col] == board_copy[2][col] == win:
                return True

        for row in range(3):
            if board_copy[row][0] == board_copy[row][1] == board_copy[row][2] == win:
                return True

            # asc diagonal win check
        if board_copy[2][0] == board_copy[1][1] == board_copy[0][2] == win:
            return True

            # desc diagonal win chek
        if board_copy[0][0] == board_copy[1][1] == board_copy[2][2] == win:
            return True

        return False
