'''
***** DOES NOT WORK *****

[
  [inf, -1, -1, 0]
  [inf, inf, inf, inf]
  [-1, -1, -1, -1]
  [-1, -1, inf, -1]
]
[(1,1),()] ->
[(0,0),(1,0)]
{(0,0),(1,0)}
[
  [5, -1, -1, 0]
  [4, 3, 2, 1]
  [-1, -1, -1, -1]
  [-1, -1, inf, -1]
]

1. How are we going to traverse our 2D grid?
  - traverse mXn grid using a nested for loop untill we hit an inf value
2. When we find an inf value, how are we going to find the closest 0 value
  - BFS traversal, as we traverse, if we hit another inf value, we push the coordinates of the 
  current value onto a seen stack and then move to the next value
3. How are we going to fill in each instance of inf with the number of spots between that spot
    and the closet 0
  - if we hit a number that is greater than 0, then the current space is x+1 away from the closest 
  tresure chest so we can fill in that value
  - Once we hit a value that is greater than or equal to 0 and is less than inf, then we loop through
  our seen stack (top to bottom) and fill in values from 0 - len(stack)
  
1. init bfs traversal fn
  - init seenStack and q deque
  - iterate while q
  - popleft from bottom of q -> 
    - if value is -1 then continue 
    - if value is inf, continue through bfs traversal until you hit another inf value -> store current
      inf value coordinates on seen STack
    - if value is between 0 and inf, then interate through seenStack and apply val-n to each item in seen
2. create row/col for loops to iterate through 2D list
3. Once iteration is complete, reeturn 2D list 

'''

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
      INF=2147483647
      directions = [[1,0],[-1,0],[0,1],[0,-1]]

      def findTreasure(row,col):
        q, seen = deque([(row,col)]), []

        while q:
          row,col = q.popleft()
          print(row,col)
          
          if grid[row][col] == INF:
            for dr,dc in directions:
              if(
                (row+dr) in range(len(grid))
                (col+dc) in range(len(grid[0]))
                and grid[row+dr][col+dc] >= 0):
                print(q)
                if grid[row+dr][col+dc] >=0 and grid[row+dr][col+dc] < INF:
                  seen.append((row,col))
                  spotsAway = grid[row+dr][col+dc]
                  for i in range(seen):
                    grid[seen[i][0]][seen[i][1]] = spotsAway - i
                  break
                
                q.append((row+rc, col+dc))
                seen.append((row,col))

      for row in range(len(grid)):
        for col in range(len(grid[0])):
          if grid[row][col] == INF:
            print("awef")
            findTreasure(row,col)
        
        return grid
        





        