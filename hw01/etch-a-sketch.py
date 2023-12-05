!#/home/bin/env python3
def printboard(arr):
    for i in range(len(arr)):
        
        for j in range(len(arr[i])):
            print(arr[i][j], end = " ")
        print()
        
def clearboard(arr):
    for i in range(len(arr)):
        
        for j in range(len(arr[i])):
            arr[i][j] = '.'

print("Welcome to Etch-a-sketch")
com = input("Number of Rows: ")
rows = int(com)
com = input("Number of Columns: ")
cols = int(com)

board = [["." for i in range(cols)] for j in range(rows)]


curr = [0,0]
print("Controls:")
print("w = MOVE UP, s = MOVE DOWN, a = MOVE RIGHT, d = MOVE LEFT, space = CLEAR BOARD")
print("hit enter after move to submit")
print("Note: clearing board does not reset currsor (just like a real etch-sketch")

while True:
    board[curr[0]][curr[1]] = 'X'
    printboard(board)
    com = input("Move:")
    if com == "w" and curr[0] > 0:
        curr[0] = curr[0] - 1
    elif com == "s" and curr[0] < cols -1:
        curr[0] = curr[0] + 1
    elif com == "a" and curr[1] > 0:
        curr[1] = curr[1] - 1
    elif com == "d" and curr[1] < rows - 1:
        curr[1] = curr[1] + 1
    elif com ==" ":
        clearboard(board)
    else:
        print("not a valid move")
