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
    """

    for line in board:
        for element in line:
            if element != '*' and \
               element != ' ' and \
               element not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
                return False

    return True

def validate_columns(board: list):
    '''
    Check if the columns are constructed according to the rules.
    '''

    transposed_board = [[board[jindex][index] for jindex in range(len(board))]
                        for index in range(len(board[0]))]

    if not validate_rows(transposed_board):
        return False

    return True

def validate_rows(board: list):
    '''
    Check if the rows are constructed according to the rules.
    '''

    for line in board:
        if not check_row(line):
            return False

    return True

def validate_colors(board: list):
    '''
    Check if colors are constructed according to the rules.
    '''

    for index in range(9):
        horizontal_color = board[-1-index]
        vertical_color = [board[index][jindex] for jindex in range(9) ]
        color_list = vertical_color + horizontal_color
        if not check_row(color_list):
            return False

    return True

def check_board(board: list):
    '''
    Check if the board is constructed according to the rules.
    '''
    if not validate_rows(board) or \
       not validate_columns(board) or \
       not validate_colors(board):
        return False

    return True

if __name__ == '__main__':
    board_input = read_board(input('Enter path to a file: '))
    print(check_board(board_input))
