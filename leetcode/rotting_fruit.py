'''
[
  [0,1,2,1]
  [0,1,2,2]
  [0,1,2,1]
]
t=2

1. How are we going to traverse through the 2d grid to find all of the rotten fruit?
  - nXm iteration of the grid o(nXm)
2. How are we going to get the state of the grid after each second?
  - Perform a BFS search on the grid starting at all of the rotten fruit spots in the grid.  At each iteration of the search,
      we can flip the number that sits in a fresh fruit spot if it is going to turn rotten that second.  when we perform our BFS search, we 
      can ignore empty and rotten fruits?
3. How are we going to know when all fruit within the grid is rotten?
  -if we ever find our BFS queue empty, it means that all fruit within the grid is rotten because we do not add any empty or rotten spaces
    to the queue.  There may still be fresh fruit in the grid after the BFS search, however if there is it means that the fresh fruit has not
    been affected by any rotten fruit
4. How are we going to keep track of the number of seconds it takes before all fruit is rotten?
  - As we iterate through our queue, we can have a counter that counts the number of iterations which would represent the number of seconds
  it took to turn all fresh fruit into rotten fruit

1. Init queue variable=deque, secondCount=0, visisted=set() 
2. iterate through the grid and find all rotten fruit coordinates and insert them into the q and visisted datasets
3. bfs search while len(q)>0:
  3.1 pop bottom item off queue
  3.1.2 turn that space into rotten fruit
  3.2 Loop through the neighbors of the space that we just popped from the queue
  3.3 If the space contains fresh fruit and we have not visited it, push it on the queue to turn rotten on the next iteration.  Also insert
    the coordinates onto the visited set
  3.3.increase the secondCount variable
4. return the secondCount after the BFS traversal has completed

Multi-source BFS
'''

'''
This problem presents us with a 2D grid that contains three different values, 0 which represents an empty cell, 1 which 
represents a fresh fruit, and 2 which represents a rotten fruit.  The problem states that each second, every fresh fruit 
that is horizontally or vertically adjacent to a rotten fruit will become rotten.  The problem asks us to find the 
number of seconds it takes for every fruit within the grid to turn rotten.  If it is impossible to turn every fruit in 
the grid rotten (aka there is a fresh fruit that dose not touch any rotten fruit and therefore will not turn rotten), 
then return -1.

To solve this problem, we must find every instance of rotten fruit in the grid and then, each second, convert all of 
that rotten fruit’s fresh fruit neighbors into rotten fruit.  This can be done using a BFS search of the grid using the 
rotten fruit as a starting point.  Because it is possible for there to be more than one rotten fruit starting point, we 
can use a multi-source BFS solution.  When implemented, we will know that every fresh fruit connected with any rotten 
fruit will have turned rotten when our BFS queue is empty after performing our BFS search.  However, because it is 
possible for fresh fruit to remain untouched, we can keep a fresh fruit counter to determine if there are any fresh 
fruit remaining in the grid after the BFS search.  If any fresh fruit remains, we return -1.
'''
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
      q, secondCount, visited = deque(),  0, set()
      rowLen, colLen = len(grid), len(grid[0])
      freshCount=0
      directions = [[1,0], [-1,0], [0,1],[0,-1]] #up,down,right,left

      def addToBfsQueue(newRow,newCol):
          if(newRow in range(len(grid)) 
            and newCol in range(len(grid[0])) 
            and (newRow,newCol) not in visited 
            and grid[newRow][newCol]==1):

            q.append((newRow,newCol))
            visited.add((newRow, newCol))

      for row in range(len(grid)):
        for col in range(len(grid[0])):
          if grid[row][col] == 2:
            for dr,dc in directions:
              addToBfsQueue(row+dr,col+dc)
          elif grid[row][col] == 1:
            freshCount+=1
      
      while q:
        for _ in range(len(q)):
          row,col = q.popleft()
          freshCount-=1
          grid[row][col] = 2
          
          for dr,dc in directions:
            addToBfsQueue(row+dr, col+dc)

        secondCount+=1
      
      return secondCount if freshCount == 0 else -1

        