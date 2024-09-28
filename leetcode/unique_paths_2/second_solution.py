'''
This problem presents us with a 2D grid filled with 0s and 1s where 0s represent open spaces and 1s represent obstacles.  
The problem asks us to find the number of paths that can be made from the top left hand corner of the grid down to the 
bottom right hand corner of the grid.  The paths cannot move through obstacles and you can only move to the right and down.

The brute force solution for this problem would be to do a DFS search through the grid to find ever possible solution 
from every space within the grid.  However, because we are trying to find ALL possible paths within the grid, we will 
end up needing to visit multiple spaces multiple times if more than one valid path passes through any given space.  However, 
if we end up visiting a spot that we have already visited in another path traversal, we should already know how many 
valid paths there are from that spot, since our DFS search finds all valid paths from all spots, and if we have already 
visited a spot, it means we have already calculated the valid paths from that spot.  Therefore, we can memoize the valid 
paths from any spot we have already visited so the next time we visit that spot, we do not need to recalculate that value 
for a different path.  Because of this, we can use a dynamic programming approach to solve this problem.

Our goal for our dynamic programming approach would be to find the number of ways we can reach the bottom right hand spot 
in our grid from the top left corner.  Since we can only move to the right and down, to determine the number of ways we 
can reach the end, we must find the number of ways we can reach the end from the spot above it and the spot to the left.  
The total number of paths for the bottom right corner will be the sum of the paths coming from the left and up.  Breaking 
down the problem, that means to get to any spot in the grid, we must calculate the number of paths from the spot to the 
left and above the current spot.  Therefore, our dynamic programming approach can be a top down approach where, starting 
at the top left corner moving to the right and down, we calculate that grids path count by adding the path count from the 
space to the left and above.  However, as we calculate each spot, we must also check if that spot is an obstacle in our 
input grid.  If it is, there are no way to get to that grid, and the value of paths to that space will automatically be 0.  
Also, since our first row will not have a row above it, we only use the spot to the left of the spots we are calculating.

At first, it seems like we may be able to do this using a 2D grid for our cache.  However, as we move through the rows in 
our grid, we can start to see that, to calculate any spot, we only need that spot’s current row and the row above.  
Therefore, we can shrink the size of our cache to be two 1D arrays that match the size of our grids row size.  As we move 
through our top-down solution, we can throw away the cached rows we generated outsize of those two rows we need for 
calculating.  This shrinks the memory complexity of the solution down from O(rowsXcols) to be O(rows).  
'''

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1:
            return 0

        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        prev_row, curr_row = [0]*COLS, [0]*COLS

        prev_row[0] = 1 if obstacleGrid[0][0] == 0 else 0
        for i in range(1,COLS):
            prev_row[i] = prev_row[i-1] if obstacleGrid[0][i] == 0 else 0
        
        for r in range(1,ROWS):
            curr_row = [0]*COLS
            curr_row[0] = 0 if obstacleGrid[r][0] == 1 else prev_row[0]
            for c in range(1,COLS):
                curr_row[c] = 0 if obstacleGrid[r][c] == 1 else curr_row[c-1] + prev_row[c]
            
            prev_row = curr_row
        

        return prev_row[-1]
