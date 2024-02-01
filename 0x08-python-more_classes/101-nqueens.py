#!/usr/bin/python3
"""
finds all possible solutions the N queens puzzle, including
translations and reflections.
Attributes:
N (int): base number of queens, and length of board side in piece positions
candidates (list) of (list) of (list) of (int): list of all successful
solutions
"""
from sys import argv
if len(argv) != 2:
    print('Usage: nqueens N')
    exit(1)

if not argv[1].isdigit():
    print('N must be a number')
    exit(1)

N = int(argv[1])

if N < 4:
    print('N must be at least 4')
    exit(1)


def column_board_gen(board=[]):
    """Adds a column of zeroes to the right of any board about to be tested for
    queen arrangements in that column.
    Args:
    board (list) of (list) of (int): 2D list of ints, only as wide as
    needed to test the rightmost column for queen conflicts.
    Returns:
    modified 2D list
    """
    if len(board):
        for row in board:
            row.append(0)
    else:
        for row in range(N):
            board.append([0])
    return board


def queen_add(board, row, col):
    """Sets "queen," or 1, to coordinates given in board.
    Args:
    board (list) of (list) of (int): 2D list of ints, only as wide as
    needed to test the rightmost column for queen conflicts.
    row (int): first dimension index
    col (int): second dimension index
    """
    board[row][col] = 1


def queen_safe(board, row, col):
    """For the board given, checks that for a new queen placed in the rightmost
    column, there are no other "queen"s, or 1 values, in the martix to the
    left, and diagonally up-left and down-left.
    Args:
    board (list) of (list) of (int): 2D list of ints, only as wide as
    needed to test the rightmost column for queen conflicts.
    row (int): first dimension index
    col (int): second dimension index
    Returns:true if no left side conflicts found for new queen, or False if a
    conflict is found.
    """
    x = row
    y = col
    for i in range(1, N):
        if (y - i) >= 0:
            if (x - i) >= 0:
                if board[x - i][y - i]:
                    return False
            if board[x][y - i]:
                return False
            if (x + i) < N:
                if board[x + i][y - i]:
                    return False
    return True


def coor_dinate_format(candidates):
    """Converts a board (matrix of 1 and 0) into a series of row/column
    indicies of each queen/1.
    Args:
    candidates (list) of (list) of (list) of (int): list of all successful
    solutions for amount of columns last checked
    Attributes:
    holberton (list) of (list) of (int): each member list contains the row
    column number for each queen found
    Returns:
    holberton, the list of coordinates
    """
    holberton = []
    for x, attempt in enumerate(candidates):
        holberton.append([])
        for i, row in enumerate(attempt):
            holberton[x].append([])
            for j, col in enumerate(row):
                if col:
                    holberton[x][i].append(i)
                    holberton[x][i].append(j)
    return holberton


candidates = []
candidates.append(column_board_gen())
for col in range(N):
    new_candidates = []
    for matrix in candidates:
        for row in range(N):
            if queen_safe(matrix, row, col):
                temp = [line[:] for line in matrix]
                queen_add(temp, row, col)
                if col < N - 1:
                    column_board_gen(temp)
                new_candidates.append(temp)
    candidates = new_candidates
for item in coor_dinate_format(candidates):
    print(item)
