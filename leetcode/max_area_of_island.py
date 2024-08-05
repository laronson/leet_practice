'''
[
  [0,1,1,1]
  [0,1,0,0]
  [0,0,1,0]
]

1. How am I going to find an island?
  - scan the grid row by col until I find a spot with a 1.  If that spot had already been visited, do not visit it twice.
2. How am I going to find the size an island?
  - BFS interative approach
3. How am I going to prevent duplicating work to count an island twice?
  - Keep track of visited locations in BFS search and do not re-visit location if we have already visited it
4. How am I going to keep track of max island as I search the grid?
  - BFS function will return the size of the island that it is traversing and we keep track of the max returns from that function

1. init maxIsland, visited = 0, set()
2. define bfs traversal function:
  - input: row coordinate, col coordinate
  - init queue to store locations visiting in bfs search and init islandCount
  - iterate while len(q) > 0:
    - islandCount+1
    - if go up, down, left, right is 1 and has not been visited, add to queue and add to visited set 
3. iterate row and cols:
  - if grid[r][c] == 1 and has not been visited, then traverse island
  - max(maxIsland, returnedFromTraversale)
'''
'''
This problem presents us with a 2D grid containing 0s and 1s where 0s represent water and 1s represent land.  The 
problem asks us to find the island with the max area of land and return that max value.

To do this, we need to scan the 2D grid for all islands.  When we find an island, we can use a BFS search of that island 
to scan the neighbors of all spots contained within that island.  As we scan the neighbors of any spot within the 
island, we add that location to both a queue that is keeping track of all of the places we need to traverse through in 
our BFS search AND we need to add that location to a visited set to make sure we do not visit a location twice.  If the 
neighboring spot to a spot we are traversing has already been visited, we do not add it to our traversal queue.  As we 
traverse through our BFS search, every time we pop a value off of our queue (aka scan a new spot on the island) we 
increase a count of island area to keep track of the size of that island.  We return this size value from the BFS search 
function. 

Finally, to scan the entire grid, we loop through every spot in the list until we find a spot of land that we have not 
visited in any of our traversals of any other islands.  If we find a spot that meets this criteria, perform a BFS 
traversal to find the size of that island and compare the returned size to the maxSize we have already seen.  Once we 
have scanned the entire grid, we return the max island size that we have seen.
'''
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
      maxIsland, visited = 0, set()
      directions = [(0,1),(0,-1),(1,0),(-1,0)]

      def getIslandSize(row,col):
        q, islandSize = deque([(row,col)]), 0
        visited.add((row,col))

        while q:
          r,c = q.popleft()
          islandSize+=1

          for rowDirection, colDirection in directions:
            newRow, newCol = r + rowDirection, c + colDirection
            if(
              newRow in range(len(grid)) and newCol in range(len(grid[0]))
              and (newRow,newCol) not in visited
              and grid[newRow][newCol] == 1):
              q.append((newRow,newCol))
              visited.add((newRow,newCol))

        return islandSize
      
      for row in range(len(grid)):
        for col in range(len(grid[0])):
          if (row,col) not in visited and grid[row][col] == 1:
            islandSize = getIslandSize(row,col)
            maxIsland = max(islandSize, maxIsland)
      
      return maxIsland


        