# Validate given board including dimension,value,rules
def validateBoard(board):

    if len(board) != 9:
        raise ValueError("Board must contain exactly 9 rows")

    for row in board:
        if len(row) != 9:
            raise ValueError("Each row must contain exactly 9 values")
    
    for row in board:
        for value in row:
            if type(value) != int or value not in range(10):
                raise ValueError("Values should be integers from 0 to 9")

    for index,row in enumerate(board):
        seen = set()
        for value in row:
            if value == 0:
                continue
            if value in seen:
                raise ValueError(f"Duplicate value {value} in row {index + 1}")
            seen.add(value)

    for col in range(9):
        seen = set()

        for row in range(9):
            value = board[row][col]
            if value == 0:
                continue
            if value in seen:
                raise ValueError(f"Duplicate value {value} in column {col + 1}")
            seen.add(value)

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            seen = set()
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    value = board[row][col]
                    if value == 0:
                        continue

                    if value in seen:
                        raise ValueError(f"Duplicate value {value} in 3x3 box starting at row {i + 1}, column {j + 1}")
                    seen.add(value)


# Check if the number placement is safe or not
def isSafe(board, row, col, num):
    for x in range(9):
        if board[row][x] == num:
            return False

    for x in range(9):
        if board[x][col] == num:
            return False

    startRow = row - (row % 3)
    startCol = col - (col % 3)

    for i in range(3):
        for j in range(3):
            if board[i + startRow][j + startCol] == num:
                return False

    return True

def solveSudokuRecursive(board, row = 0, col = 0):  
    if row == 9:
        return True

    if col == 9:
        return solveSudokuRecursive(board, row + 1, 0)

    if board[row][col] != 0:
        return solveSudokuRecursive(board, row, col + 1)

    for num in range(1, 10):
        if isSafe(board, row, col, num):
            board[row][col] = num

            if solveSudokuRecursive(board, row, col + 1):
                return True

            board[row][col] = 0

    return False

def solveSudoku(board):
    validateBoard(board)
    return solveSudokuRecursive(board)
