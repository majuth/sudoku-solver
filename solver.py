def numInRow(arr, row, num):
    for clm in range(9):
        if (arr[row][clm]==num):
            return True
    return False

def numInCol(arr, col, num):
    for rw in range(9):
        if (arr[rw][col]==num):
            return True
    return False

def numInBox(arr, row, col, num):
    startRowBox = row - (row % 3)
    startColBox = col - (col % 3)
    for currRow in range(startRowBox, startRowBox+3):
        for currCol in range(startColBox, startColBox+3):
            if (arr[currRow][currCol]==num):
                return True
    return False


def isNumValid(arr, row, col, num):
    return not (numInRow(arr, row, num) or numInCol(arr, col, num) or numInBox(arr, row, col, num))

def findNextEmptyspot(arr,currSpot):
    for row in range(9):
        for col in range(9):
            if(arr[row][col]==0):
                currSpot[0]=row
                currSpot[1]=col
                return True
    return False

def print_grid(arr):
    for i in range(9):
        for j in range(9):
            print (arr[i][j], end=" ")
        print ("", end="\n")


def sudokuSolver(arr):

    currSpot = [0,0]

    if findNextEmptyspot(arr, currSpot) == False:
        return True
    
    row = currSpot[0]
    col = currSpot[1]

    for num in range(1, 10):
         
        if(isNumValid(arr, row, col, num)):
             
            arr[row][col]=num
 
            if(sudokuSolver(arr)):
                return True
 
            arr[row][col] = 0
                  
    return False

if __name__=="__main__":

    grid =[[0 for x in range(9)]for y in range(9)]
     
    grid =[[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]
     
    if(sudokuSolver(grid)):
        print_grid(grid)
    else:
        print ("No sudoku solution exists")
