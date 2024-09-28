'''
inputs:
    - obsticalGrid:List[List[int]] : an mxn grid filled with 0s and 1s where a 0 represents an open space and a 1 represents an obstical
    - return: int -> The number of ways a robot could move from the top left hand corner of the grid (obsticalGrid[0][0]) to the bottom right hand corner of the grid 
    (obstical grid[m-1][n-1])

Rules:
    - A robot cannot move anywhere that is not in the grid
    - A robot cannot move anywhere that is filled with an obstial 
    - A robot can only move to the right or downard

grid:
[
       0 1 2 3
    0 [10 6 3 1]
    1 [4 3 2 1]
    2 [1 1 1 d]
]
res: 4

grid:
[
       0 1 2 3 4
    0 [0 0 0 0 0]
    1 [0 1 0 1 0]
    2 [0 0 1 0 0]
]
cache:
[
       0 1 2 3 4
    0 [1 1 1 1 1]
    1 [0 0 0 0 1]
    2 [0 0 0 1 0]
]
res: 4

1) init cache to be the same size as obstical grid filled with 0s
2) init last col of cache to be 1 unless blocked by obstical and init last row of cache to be 1 unless blocked by obstical
3) starting at index [m-2][n-2], loop backwards to calculate number of available paths at each space based on spaces below
    3a) if index is at a spot with an obstical keep at 0
    3b) add cache at spot below and spot to the right to get number of available paths at that point
4) return value at cache [0][0]
'''

'''
This solution works, but it uses a 2D matrix for the cache when in reality we only need two 1D lists.  This is because, when
we calculate the number of paths from any given space, we only need the values from the row that space is in, and the row
that we previously calculated.  There is no need to store every row in memory once we have calculated it because once it has
been calculated, and it has been used to calculate the next row, it is no longer needed.
'''

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        cache = [[0]*COLS for _ in range(ROWS)]

        obsticalHit = False
        for idx in range(COLS-1,-1,-1):
            if obstacleGrid[ROWS-1][idx] == 1:
                obsticalHit = True
            cache[ROWS-1][idx] = 1 if not obsticalHit else 0

        obsticalHit = False
        for r in range(ROWS-1,-1,-1):
            if obstacleGrid[r][COLS-1] == 1:
                obsticalHit = True
            cache[r][COLS-1] = 1 if not obsticalHit else 0
        
        print(cache)
        for r in range(ROWS-2, -1,-1):
            for c in range(COLS-2,-1,-1):
                if obstacleGrid[r][c] == 1:
                    continue
                
                cache[r][c] = cache[r+1][c] + cache[r][c+1]
        
        return cache[0][0]


        