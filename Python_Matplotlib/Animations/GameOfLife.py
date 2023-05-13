from typing import List
from random import randint

class GameOfLife:
    def __init__(self, rows:int, columns:int):
        self.board = [[randint(0, 1) for j in range(columns)] for i in range(rows)]
        # self.board = [[0] * columns for i in range(rows)]
        # self.board[int(rows/2)][int(columns/2)] = 1

    def cellNextState(self, i, j, board: List[List[int]]) -> bool:
        i_min = i if i == 0 else i - 1
        i_max = i if i == len(board) - 1 else i + 1
        j_min = j if j == 0 else j - 1
        j_max = j if j == len(board[0]) - 1 else j + 1

        counter = 0

        for line in range(i_min, i_max + 1, 1):
            for col in range(j_min, j_max + 1, 1):
                if line == i and col == j:
                    continue
                if board[line][col] == 1:
                    counter += 1
        
        if board[i][j] == 0 and counter == 3:
            return True

        if board[i][j] == 1 and (counter < 2 or counter > 3):
            return True

        return False
    
    def boardNextState(self) -> None:
        changes = []

        for i in range(0, len(self.board), 1):
            for j in range(0, len(self.board[0]), 1):
                if self.cellNextState(i, j, self.board) == True:
                    changes.append([i, j])

        for k in changes:
            line = k[0]
            col = k[1]
            self.board[line][col] = 0 if self.board[line][col] == 1 else 1

    def __str__(self):
        board_string = ""
        for i in self.board:
            for j in i:
                board_string += str(j)
            board_string += "\r\n"
        return board_string

    def getNextBoardState(self) -> List[List[int]]:
        self.boardNextState()
        return self.board

    def getBoardSize(self) -> tuple[int, int]:
        rows = len(self.board)
        columns = len(self.board[0])
        return (rows, columns)
    