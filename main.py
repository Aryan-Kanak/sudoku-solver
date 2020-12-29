# This code was written by Aryan Kanak

# displays grid
def display_grid(grid):
    for i in range(9):
        print('|', end='')
        for j in range(9):
            print(grid[i][j], end='|')
            if j == 2 or j == 5:
                print(' |', end='')
        print()
        if i == 2 or i == 5:
            for j in range(23):
                print('-', end='')
            print()


# checks if a number can be placed in a certain row
def valid_row(grid, num, row):
    valid = True
    for i in range(9):
        if grid[row][i] == num:
            valid = False
            break

    return valid


# checks if a number can be placed in a certain column
def valid_column(grid, num, column):
    valid = True
    for i in range(9):
        if grid[i][column] == num:
            valid = False
            break

    return valid


# checks if a number can be placed in a certain box
def valid_box(grid, num, row, column):
    valid = True
    for i in range(row - (row % 3), row - (row % 3) + 3):
        for j in range(column - (column % 3), column - (column % 3) + 3):
            if grid[i][j] == num:
                valid = False
                break

    return valid


# checks if a number can be placed in a certain square
def valid_square(grid, num, row, column):
    return valid_row(grid, num, row) and valid_column(grid, num, column) and valid_box(grid, num, row, column)


# returns the row and column index of the next square or false if there is none
def next_square(row, column):
    if column != 8:
        return row, column + 1
    elif row != 8:
        return row + 1, 0
    else:
        return False


# solves a single square and all squares following it
def solve_square(grid, row, column):
    # get index of next square
    next_sqr = next_square(row, column)

    # if square is already solved
    if grid[row][column] != ' ':
        # if whole grid is solved
        if not next_sqr:
            return grid
        else:
            return solve_square(grid, next_sqr[0], next_sqr[1])
    else:
        # check all possible numbers to find a valid one
        for i in range(1, 10):
            if valid_square(grid, str(i), row, column):
                grid[row][column] = str(i)
                # if whole grid is solved
                if not next_sqr:
                    return grid
                else:
                    solved_grid = solve_square(grid, next_sqr[0], next_sqr[1])
                    # backtrack if an invalid solution has been found
                    if not solved_grid:
                        grid[row][column] = ' '
                    # return valid solution
                    else:
                        return solved_grid

        # return False if there is no valid solution
        return False


# solves a sudoku grid
def solve_grid(grid):
    return solve_square(grid, 0, 0)


# tests
test0 = [[' ', ' ', ' ', '2', '6', ' ', '7', ' ', '1'],
         ['6', '8', ' ', ' ', '7', ' ', ' ', '9', ' '],
         ['1', '9', ' ', ' ', ' ', '4', '5', ' ', ' '],
         ['8', '2', ' ', '1', ' ', ' ', ' ', '4', ' '],
         [' ', ' ', '4', '6', ' ', '2', '9', ' ', ' '],
         [' ', '5', ' ', ' ', ' ', '3', ' ', '2', '8'],
         [' ', ' ', '9', '3', ' ', ' ', ' ', '7', '4'],
         [' ', '4', ' ', ' ', '5', ' ', ' ', '3', '6'],
         ['7', ' ', '3', ' ', '1', '8', ' ', ' ', ' ']]
test1 = [[' ', '2', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', '6', ' ', ' ', ' ', ' ', '3'],
         [' ', '7', '4', ' ', '8', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', '3', ' ', ' ', '2'],
         [' ', '8', ' ', ' ', '4', ' ', ' ', '1', ' '],
         ['6', ' ', ' ', '5', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', '1', ' ', '7', '8', ' '],
         ['5', ' ', ' ', ' ', ' ', '9', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', '4', ' ']]

# enter the puzzle to be solved below into the variable sudoku_grid
sudoku_grid = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
display_grid(sudoku_grid)

# solve sudoku grid
solution = solve_grid(sudoku_grid)

# if there is no valid solution
if not solution:
    print("This sudoku puzzle is impossible!")
# display solution
else:
    print("Solution:")
    display_grid(solution)
