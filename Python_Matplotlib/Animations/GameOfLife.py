from typing import List
from random import randint

class GameOfLife:
    def __init__(self, rows:int, columns:int, loop:bool):
        self.board = [[randint(0, 1) for j in range(columns)] for i in range(rows)]
        self.loop = loop

    def cellNextState(self, i, j) -> bool:
        counter = 0

        if self.loop == False:        
            i_min = i if i == 0 else i - 1
            i_max = i if i == self.getBoardSize()[0] - 1 else i + 1
            j_min = j if j == 0 else j - 1
            j_max = j if j == self.getBoardSize()[1] - 1 else j + 1

            for line in range(i_min, i_max + 1, 1):
                for col in range(j_min, j_max + 1, 1):
                    if line == i and col == j:
                        continue
                    if self.board[line][col] == 1:
                        counter += 1
        else:
            print("Check cell in row {}, col{}".format(i, j))
            for line in range(i - 1, i + 2, 1):
                for col in range(j - 1, j + 2, 1):
                    actual_line = line % self.getBoardSize()[0]
                    actual_col  = col  % self.getBoardSize()[1]
                    print("Actual line = {}\r\nActual column = {}".format(actual_line, actual_col))
                    if actual_line == i and actual_col == j:
                        continue
                    if self.board[actual_line][actual_col] == 1:
                        counter += 1

        if self.board[i][j] == 0 and counter == 3:
            return True

        if self.board[i][j] == 1 and (counter < 2 or counter > 3):
            return True

        return False
    
    def boardNextState(self) -> None:
        changes = []

        for i in range(0, len(self.board), 1):
            for j in range(0, len(self.board[0]), 1):
                if self.cellNextState(i, j) == True:
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
    