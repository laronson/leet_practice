'''
***** THIS IS NOT A WORKING SOLUTION *****

 [
  [.,Q,.,.],
  [.,.,.,q],
  [q,.,.,.]
  [.,.,q,.]
 ]
 (row,0),(1,col),diag

 1. How do I keep track of where I can or cannot place a queen based off of other queens on the board?
  - Keep track of spaces where queens exist in a set of (row,col) pairs
  - Check if any queen exists in grid at that column location in any row above the current location
  - check if any queen exists at row-n,col-n to check diagnol spaces
 2. How am I going to traverse a grid of size n to determine where I can place a queen
  - DFS recursive solution o(n^2)
  - We add queens to our grid row by row because we know two queens cannot exist in the same row
  - When we add a queen, immediately start looking for a spot in a new row moving from top of grid to bottom of grid
 3. How am I going to store the graphical representation of a board to return 
  - Implement a printGrid functuoin that takes a list of queens and prints a grid based off of the location of queens
'''

class Solution:
    def willHitDiagnol(self,queens,n,row,col):
      for i in range(1,n-row):
        if (row+i,col-i) in queens or (row-i,col-i) in queens:
          return True
      return False

    def willHitUp(self,queens,n,row,col):
      for i in range(1, n-row):
        print(i, row,col,queens)
        if (row-i,col) in queens:
          return True
      return False
    
    def printGrid(self,queens,n):
      grid = []
      for i in range(n):
        row = ""
        for j in range(n):
          if (i,j) in queens:
            row += "Q"
          else:
            row += '.'
        grid.append(row)
      return grid
        

    def solveNQueens(self, n: int) -> List[List[str]]:
      res,qLoc = [],[]

      def dfs(queens, row, col):
        if row not in range(n) or col not in range(n):
          res.append(self.printGrid(queens,n))
          return

        if self.willHitDiagnol(queens,n,row,col) or self.willHitUp(queens,n,row,col):
          dfs(queens,row,col+1)

        queens.append((row,col))
        dfs(queens, row+1,0)
        queens.pop()
      
      dfs([],0,0)
      return res
        