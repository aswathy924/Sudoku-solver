import pytest

from src.solver import (
    validateBoard,
    isSafe,
    solveSudoku,
)

@pytest.fixture
def puzzle():
    return [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]


def test_valid_board(puzzle):
    assert validateBoard(puzzle) is None


def test_invalid_board_dimensions():
    with pytest.raises(ValueError):
        validateBoard([[0, 0, 0]])


def test_duplicate_in_row():
    board = [[0] * 9 for _ in range(9)]
    board[0][0] = 5
    board[0][1] = 5
    with pytest.raises(ValueError):
        validateBoard(board)


def test_is_safe(puzzle):
    assert isSafe(puzzle, 0, 2, 4) is True
    assert isSafe(puzzle, 0, 2, 5) is False


def test_solves_puzzle(puzzle):
    assert solveSudoku(puzzle) is True
    for row in puzzle:
        assert set(row) == set(range(1, 10))


def test_invalid_values():
    board = [[0] * 9 for _ in range(9)]
    board[0][0] = 10

    with pytest.raises(ValueError):
        validateBoard(board)


def test_duplicate_in_column():
    board = [[0] * 9 for _ in range(9)]
    board[0][2] = 5
    board[3][2] = 5

    with pytest.raises(ValueError, match="column 3"):
        validateBoard(board)


def test_duplicate_in_subgrid():
    board = [[0] * 9 for _ in range(9)]
    board[0][0] = 5
    board[1][1] = 5

    with pytest.raises(ValueError, match="3x3 box"):
        validateBoard(board)


def test_rejects_wrong_row_length():
    board = [[0] * 9 for _ in range(9)]
    board[4] = [0] * 8
    with pytest.raises(ValueError, match="9 values"):
        validateBoard(board)


def test_rejects_invalid_value():
    board = [[0] * 9 for _ in range(9)]
    board[0][0] = 10

    with pytest.raises(ValueError, match="integers from 0 to 9"):
        validateBoard(board)


def test_rejects_non_integer_value():
    board = [[0] * 9 for _ in range(9)]
    board[0][0] = 2.5

    with pytest.raises(ValueError, match="integers from 0 to 9"):
        validateBoard(board)

def test_unsolvable_puzzle():
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    board[0][2] = 1
    board[0][3] = 2

    assert solveSudoku(board) is False