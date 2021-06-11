def numInRow(arr, row, num):
    for col in range(9):
        if (arr[row][col]==num):
            return True
    return False

def numInCol(arr, col, num):
    for row in range(9):
        if (arr[row][col]==num):
            return True
    return False

def numInBox(arr, row, col, num):
    startRowBox = row - (row % 3)
    startColBox = col - (col % 3)
    for currRow in range(startRowBox, startColBox+3):
        for currCol in range(startColBox, startColBox+3):
            if (arr[currRow][currCol]==num):
                return True
    return False

def isNumValid(arr, row, col, num):
    not (numInRow(arr, col, num) or numInCol(arr, col, num) or numInBox(arr, row, col, num))