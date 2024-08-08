'''
n=4
[
  "Q....",
  "....Q",
  ".Q...",
  "...Q."
]

1. How are we going to put queens on the board?
  - DFS traversal
2. How are we going to determine if a space is valid or invalid?
  - Place queens row by row
  - Keep track of columns where we have placed a queen already
  - We can index our diagnols using the equation r-c for negetive diagnols and r+c for positive diagnols because the index will stay constant
    for any space within that diagnol
3. How are we going to keep track of the graphical representation of our board?
  - Use a pre-defined empty board, change the contents of the board when we place a queen, and when we reach a solution, we copy the contents
    of the board into a results list.

1. init our col, posDiagnol, and negDiagnol sets and init results list
2. init our graphical reprsentation of our board
3. init our dfs traversal functions (recursive)
  3.1: inputs: row number
  3.2: break case: if row number is greater than n then copy board into results and return
  3.3: branching logic: iterate from 0-n to try to add a queen to all col spots within the row.
    - If row,col combo is in col, posDiagnol, negDiagnol sets, then continue iterating from 0-n
    - If not in any of our sets, add queen to board, add spots to position sets, call recursive function with next row
    - on return of recursive call, remove queen from board in previous position and remove row,col combos from position sets
4. Call dfs traversal on row 0
5. return results list
'''

'''
This problem presents us with an integer value, n, that represents the number of queens that should be placed on an nXn 
grid.  The queens should be placed such that no queen can take out any of the other queens in a single move 
(up/down, left/right and diagonally).

Some rules we can immediately infer is that we cannot place a queen in the same row or column as another queen.  To help 
us place queens according to these rules, we can place our queens in a row by row manner and keep track of the columns 
that queens are placed in to reference when we are about to place a queen. We must also keep track of the diagonal paths 
of previously placed queens as well.  To do this, we must recognize that there are two types of diagonal paths: One type 
that moves in an upward to the right direction (positive) and another that moves downward to the right (negative).  We 
can index these two types of diagonal paths using the algorithms row+col for positive paths and row-col for negative 
paths.  We can do this because, for all spots within a given positive or negative diagonal path, those algorithms will 
produce the same value for all row, col combos in that path.  Therefore, as we add queens to our board, we can add the 
index of the positive and negative paths on which they sit and when we go to add another queen to the board, we can 
check to see if we are about to add that queen to a diagonal path that already has a queen.  

To solve this problem, we must first understand how we can move throughout a board of nXn size and determine where we 
can place queens in a way that they cannot be taken out by any other queen on the board in one move.  To do this, it 
makes sence to use a DFS of the board in order to find all possible queen placements for a given n value.  Because we 
are trying to find all possible solutions, a recursive backtracking solutions make sense.  When we make a call to the 
recursive function with a row that is equal to our n value, it means that we have placed all queens and we can copy our 
board into a results list.  As we traverse through the board row by row, we can iterate from 0-n to place queens within 
that row at each col value.  Before we add a queen, we check to see if that placement will conflict with any of the 
other queens we have already placed.  If the placement causes a conflict, we continue our iteration.  If we have found a 
valid spot for a queen, we add the queens position to our board, and keep track of the col and diag rules we stated 
above.  We then call our recursive fn with the next row.  When returning from the recursive function, we remove the 
queen we added to our board before the call and any of the rules and then continue to try to place queens in the 
remainder of the row.
'''
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
      cols, posDiag, negDiag = set(), set(), set()
      res = []
      board = [["."]*n for _ in range(n)]

      def addQueens(row):
        if row == n:
          b = ["".join(r) for r in board]
          res.append(b)
        
        for col in range(n):
          if col in cols or (row+col) in posDiag or (row-col) in negDiag:
            continue
          
          board[row][col] = "Q"
          cols.add(col)
          posDiag.add(row+col)
          negDiag.add(row-col)

          addQueens(row+1)

          board[row][col] = "."
          cols.remove(col)
          posDiag.remove(row+col)
          negDiag.remove(row-col)
        
      addQueens(0)
      return res


        