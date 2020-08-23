
import math, re

def sudoku_check(board):
    """Checks an NxN Sudoku Board and determines/returns whether
    or not it is a valid solution"""
    nums = len(board)
    n = int(math.sqrt(nums)) #to keep track of nxn sub-grids

    # Index variables to keep track of checking Squares
    row_count = 0
    col_count = 0

    for i in range(nums):
        if col_count == nums:
            col_count = 0
        if row_count == nums:
            row_count = 0
            col_count += n
        row = []
        column = []
        square = []
        for j in range(nums):
            # Check for valid number
            if board[i][j] < 1 or board[i][j] > nums:
                return False

            # Check for duplicate in row
            if board[i][j] in row:
                return False
            row.append(board[i][j])

            # Check for duplicate in column
            if board[j][i] in column:
                return False
            column.append(board[j][i])

            # Check for duplicate in box/square
            if board[row_count][col_count] in square:
                return False
            square.append(board[row_count][col_count])
            col_count += 1

            # Check next row, same columns
            if col_count % n == 0:
                row_count += 1
                col_count -= n

    return True

def read_from_file(from_file):
    """Takes a file to read a list of numbers from, sorts the numbers
    in descending order, then writes the sorted list to a new file"""
    board = []
    rgx = re.compile("(\w[\w']*\w|\w)")
    with open(from_file) as file:
        for line in file:
            row = rgx.findall(line)
            for x in range(len(row)):
                row[x] = int(row[x])
            board.append(row)
    return sudoku_check(board)


''' TESTING BOARD EXAMPLE
list = [[1,2,3,4,5,6,7,8,9],
        [4,5,6,7,8,9,1,2,3],
        [7,8,9,1,2,3,4,5,6],
        [3,1,2,6,4,5,9,7,8],
        [6,4,5,9,7,8,3,1,2],
        [9,7,8,3,1,2,6,4,5],
        [2,3,1,5,6,4,8,9,7],
        [5,6,4,8,9,7,2,3,1],
        [8,9,7,2,3,1,5,6,4]]

print(sudoku_check(list))'''

'''TESTING EXAMPLE: BOARD READ FROM FILE
print(read_from_file("data.txt"))'''

