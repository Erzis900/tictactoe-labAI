"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                count += 1
    
    if count % 2 == 1:
        return X
    else:
        return O
        

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possibleActions.add((i, j))

    return possibleActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    boardCopy = copy.deepcopy(board)
    boardCopy[action[0]][action[1]] = player(board)
    return boardCopy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            return board[i][0]

    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not None:
            return board[0][j]
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[2][0] == board[1][1] == board[0][2] and board[2][0] is not None:
        return board[2][0]
    
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    filledSquares = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                filledSquares += 1

    if winner(board) is not None or filledSquares == 9:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        return max_value(board)[1]
    else:
        return min_value(board)[1]


def max_value(board):
    if terminal(board):
        return utility(board), None

    v, move = float('-inf'), None
    for action in actions(board):
        score = min_value(result(board, action))[0]
        if score > v:
            v, move = score, action
            if v == 1:
                break

    return v, move

def min_value(board):
    if terminal(board):
        return utility(board), None

    v, move = float('inf'), None
    for action in actions(board):
        score = max_value(result(board, action))[0]
        if score < v:
            v, move = score, action
            if v == -1:
                break

    return v, move