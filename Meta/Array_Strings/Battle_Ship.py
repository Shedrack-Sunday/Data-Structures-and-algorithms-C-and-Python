'''
There is a matrix with . and X, where X represents battleship, always of length 3. Battleship can be vertical or horizontal, never diagonal. Given a function bomb_at(i,j), returns True if battleship is present at (i,j) in the matrix. Print the head, middle, tail coordinates of the battleship.

I asked a question to clarify, and as it turns out there will always be one battleship.

.........
.....X...
.....X...
.....X...
.........

Here’s how we could write the function:

We’ll search for an X that represents the head of the battleship.
Once the head is found, check if the battleship is oriented vertically or horizontally by checking adjacent cells.
After determining the direction, print the coordinates of the head, middle, and tail of the battleship.

'''

def find_battleship(board):
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'X':
                if i + 1 < len(board) and board[i +1][j] == 'X':
                    head = (i, j)
                    middle = (i + 1, j)
                    tail = (i + 2, j)
                elif j + 1 <len(board[0]) and board[i][j +1] == 'X':
                    head = (i, j)
                    middle = (i, j + 1)
                    tail = (i, j + 2)
                else:
                    continue
            
                
                