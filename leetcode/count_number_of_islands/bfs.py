class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
      visited = set()
      # left, right, up, down
      directions = [[1,0],[-1,0],[0,1],[0,-1]]
      def traverseIslandBfs(r,c):
        q = deque([(r,c)])
        visited.add((r,c))

        while q:
          row,col = q.popleft()
          for dr,dc in directions:
            nRow,nCol = row+dr,col+dc
            if ((nRow) in range(len(grid))
              and (nCol) in range(len(grid[0])) 
              and (nRow,nCol) not in visited 
              and grid[nRow][nCol] == "1"):
              visited.add((nRow,nCol))
              q.append((nRow,nCol))


      islandCount=0
      for r in range(len(grid)):
        for c in range(len(grid[r])):
          if (r,c) not in visited and grid[r][c]=="1":
            print((r,c))
            traverseIslandBfs(r,c)
            islandCount+=1
      
      return islandCount