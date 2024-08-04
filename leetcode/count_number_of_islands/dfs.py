'''
1 = land
0 = water

[
  [1,1,0]
  [0,0,0]
  [1,1,1]
]

1. How are we going to traverse our grid to search for land
  - search rows X col of grid until we find a piece of unvisited land o(rowXcol)
2. How are we going to traverse an island and mark land as seen?
  - resursive backtracking 
  - Switch instances of 1 to 0 when we have seen a piece of land
3. How are we going to keep track of our island count?
  - After traversing an island and marking land locations on island as seen, increase island count by 1

1. loop through rows and cols searching for land valie
2. If land value is seen, resursively scan an island
  2.1 input: x,y coordinates of land location
  2.2 break cases: if current location is outside of grid or grid[x][y] is water
  2.3 convert grid[x][y] to water "0"
  2.4 loop up,down,left,right
3. Increase island count by 1
4. return island count
'''

'''
[
  [0,0,0]
  [0,0,0]
  [0,0,0]
]
'''

'''
This problem presents us with a 2D grid of 0s and 1s where 0 represents water and 1 represents land.  We are tasked with 
finding the number of islands within the grid.  An island is represented by an string of interconnected 1s within the 
grid.

To solve this problem, can scan the grid using a nested for loop searching is position (rowXcol) in the grid until we 
find a piece of land.  Once we find a piece of land, we can use a dfs recursive traversal to scan the rest of the 
island.  Since all of our “non-traversal” logic is determined by if we hit a piece of land or now we can ensure that we 
do not visit a piece of land twice by simply changing the values of land from 0 to 1 as we traverse an island.  The way 
in which we traverse the island would be by scanning left,right,up,down to check for a new piece of land.  Once we 
traverse a whole island, the grid should be refactored to have water whereever we had seen land during our 
islandTraversal.  We can then increase an islandCounter by 1.  Once we repeat this process through the entire grid, we 
can return the island counter.

There is another way we can traverse an island which uses an iterative bfs search.  To do this, we can use a q to keep 
track of all of the items we see in our bfs search and a visited set to keep track of which spots we have already 
visited.  If we see a value in our traversal that we have not already seen and is a piece of land, we can add the 
neighbors of that spot (that we have not already seen) to our traversal queue.  We can then iterate through our queue, 
adding new spots to the queue as we traverse and adding thsoe values to our seen set.
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
      def traverseIslandDfs(r,c):
        if r> len(grid)-1 or c> len(grid[x])-1 or r<0 or c<0 or grid[r][c]=="0":
          return
        
        grid[r][c] = "0"

        traverseIslandDfs(r+1,c)
        traverseIslandDfs(r-1,c)
        traverseIslandDfs(r,c+1)
        traverseIslandDfs(r,c-1)


      islandCount=0
      for r in range(len(grid)):
        for c in range(len(grid[r])):
          if grid[r][c] == "1":
            traverseIslandDfs(r,c)
            islandCount+=1
      return islandCount
        