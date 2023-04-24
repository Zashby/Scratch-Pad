def sudokuCheck(sudoku):
    """ Takes a massive integer (81 digits) and returns if it is a winning sudoku game"""
    check = []
    sudoku_list = []
    sudoku = list(str(sudoku))
    # Array build
    for x in range(9):
        sudoku_list.append([sudoku[x] for x in range(9)])
        if len(set(sudoku_list[x])) == 9:
            del sudoku[0:9]
        else:
            return "no"
    # vertical
    for x in range(9):
        if len(set([sudoku_list[y][x] for y in range(9)])) == 9:
            pass
        else:
            return "No"

    for y in range(0, 7, 3):
        for x in range(9):
            first, second, third = sudoku_list[x][y:y+3]
            check += first, second, third
            if len(check) == 9:
                if len(set(check)) == 9:
                    check = []
                else:
                    return "No"
    return "Yes"


print(sudokuCheck(
    295743861431865927876192543387459216612387495549216738763524189928671354154938672))

print(sudokuCheck(
    195743862431865927876192543387459216612387495549216738763524189928671354254938671))
