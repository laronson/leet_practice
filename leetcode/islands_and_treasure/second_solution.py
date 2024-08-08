'''
[
  [inf, -1, -1, 0]
  [inf, inf, inf, inf]
  [-1, -1, -1, -1]
  [-1, -1, inf, -1]
]

1. init a counter variable initilized to 0
1.5 find all zeros in the grid
2. insert zero coordingates into visited and q
3. Iterate while len(q) > 0
  4 for all values currently in the q
    4.1 pull a value off the queue, 
    4.2 chagne the value in the grid at coordinates we pulled off the queue to be the current value of the counter
    4.3 insert all inf values next to the current location (up,down,left,right) into the q
    4.4 increase counter by 1
5. return the original grid

'''

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
      counter,q,visited = 0, deque(), set()
      INF = 2147483647
      # right,left,up,down
      directions = [[1,0],[-1,0],[0,1],[0,-1]]

      for row in range(len(grid)):
        for col in range(len(grid[0])):
          if grid[row][col]==0:
            q.append((row,col))
            visited.add((row,col))
      
      while q:
        for _ in range(len(q)):
          row,col = q.popleft()
          grid[row][col] = counter
          

          for dr, dc in directions:
            newRow = row+dr
            newCol = col+dc

            if(newRow in range(len(grid))
              and newCol in range(len(grid[0]))
              and (newRow,newCol) not in visited
              and grid[newRow][newCol]==INF):
              q.append((newRow,newCol))
              visited.add((newRow,newCol))

        counter+=1
        
              

      
        





        