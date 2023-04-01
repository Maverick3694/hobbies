def solve(puzzle):
    def fnd_emptyloc(puzzle):
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] == 0:
                    return (i, j)
        return None

    def is_valid(puzzle, row, col, num):
        # Check row
        for j in range(9):
            if puzzle[row][j] == num:
                return False
        # Check column
        for i in range(9):
            if puzzle[i][col] == num:
                return False
        # Check 3x3 box
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if puzzle[i][j] == num:
                    return False
        return True

    def check(puzzle):
        empty_loc = fnd_emptyloc(puzzle)
        if empty_loc is None:
            return puzzle
        row, col = empty_loc
        for num in range(1, 10):
            if is_valid(puzzle, row, col, num):
                puzzle[row][col] = num
                if check(puzzle) is not None:
                    return puzzle
                puzzle[row][col] = 0
        return None

    return check(puzzle)
