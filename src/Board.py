"""Module which handles the creation and printing of an empty Sudoku board."""

def createBoard():
    board = []
    for _ in range(81):
        board.append(0)
    return board

def printEdgeRow():
    row = "+"
    for _ in range(3):
        row += "===|===|===+"
    row += "\n"
    return row

# Make blank spots appear instead of 0's
def printValue(value):
    if 0 == value:
        value = " "
    return str(value)

def printRowPiece(board, start):
    line = ""
    i = 0
    while i < 2:
        line += printValue(board[i + start])
        line += " | "
        i += 1
    line += printValue(board[i + start])
    line += " + "
    return line

def printRow(board, start):
    line = "+ "
    for i in range(0, 7, 3):
        line += printRowPiece(board, start + i)
    line += "\n"
    return line

def printRowSeperator():
    line = ""
    for _ in range(37):
        line += "-"
    line += "\n"
    return line

def printBoard(board):
    line = printEdgeRow()
    start = 0
    for _ in range(3):
        for _ in range(2):
            line += printRow(board, start)
            line += printRowSeperator()
            start += 9
        line += printRow(board, start)
        line += printEdgeRow()
        start += 9
    print(line)