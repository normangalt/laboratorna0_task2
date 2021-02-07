'''
Puzzle.py

GITHUB repository link:https://github.com/normangalt/laboratorna0_task2
'''

def read_board(input_path: str):
    '''
    input_path - string path to a input file
    '''

    with open(input_path, 'r', encoding = 'utf-8') as file:
        content = file.readlines()
        content = [line[:-1] for line in content[:-1]] + [content[-1]]
        return content

def check_row(board: list):
    """
    Check if a row is constructed according to the rules.

    >>> check_row([['1','2'],['3','4']])
    True
    >>> check_row([['1','1'],['3','4']])
    False
    """

    for line in board:
        for element in line:
            if (element in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0') and \
                 line.count(element) > 1):
                return False

    return True

def validate_columns(board: list):
    '''
    Check if the columns are constructed according to the rules.

    >>> validate_columns([['1','2'],['3','4']])
    True
    >>> validate_columns([['1','2'],['1','4']])
    False
    '''

    transposed_board = [[board[jindex][index] for jindex in range(len(board))]
                        for index in range(len(board[0]))]

    if not check_row(transposed_board):
        return False

    return True

def validate_rows(board: list):
    '''
    Check if the rows are constructed according to the rules.

    >>> validate_rows([['1','2'],['3','4']])
    True
    >>> validate_rows([['1','1'],['3','4']])
    False
    '''

    if not check_row(board):
        return False

    return True

def validate_colors(board: list):
    '''
    Check if colors are constructed according to the rules.

    >>> validate_colors([['1','2','2','2','2','2','2','2','2'],\
                         ['3','4','4','4','4','4','4','4','4'],\
                         ['3','4','4','4','4','4','4','4','4'],\
                         ['3','4','4','4','4','4','4','4','4'],\
                         ['3','4','4','4','4','4','4','4','4'],\
                         ['3','4','4','4','4','4','4','4','4'],\
                         ['3','4','4','4','4','4','4','4','4'],\
                         ['3','4','4','4','4','4','4','4','4'],\
                         ['3','4','4','4','4','4','4','4','4'],\
                         ['3','4','4','4','4','4','4','4','4']])
    False
    '''
    color_board = []
    for index in range(9):
        horizontal_color = board[-1-index][index:]
        vertical_color = [board[jindex][index] for jindex in range(9 - index - 1)]
        color_list = vertical_color + list(horizontal_color)
        color_board.append(color_list)

    if not check_row(color_board):
        return False

    return True

def validate_board(board: list):
    '''
    Check if the board is constructed according to the rules.
    '''
    if not validate_rows(board) or \
       not validate_columns(board) or \
       not validate_colors(board):
        return False

    return True
import doctest
doctest.testmod()
print(validate_board(read_board('input_zd2.txt')))