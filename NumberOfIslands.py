#https://leetcode.com/explore/learn/card/queue-stack/232/practical-application-stack/1380/
# According to trail 140ms and 15.3mb
# 68.05% time and 69.31% space

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.width = len(grid[0])
        self.height = len(grid)
        numIslands = 0
        for i in range(self.height):
            for j in range(self.width):
                if grid[i][j] == '1':
                    self.exploreIsland(grid,(i,j))
                    numIslands += 1
        return numIslands


    def exploreIsland(self,grid,location):
        stack = [location]
        while stack:
            loc = stack.pop(0)
            x = loc[0]
            y = loc[1]
            if grid[x][y] == '1':
                grid[x][y] = True
                if x+1 < self.height:
                    stack.append((x+1,y))
                if x-1 >= 0:
                    stack.append((x-1,y))
                if y+1 < self.width:
                    stack.append((x,y+1))
                if y-1 >= 0:
                    stack.append((x,y-1))
