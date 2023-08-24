class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] += grid[i][j-1]
                
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                
                elif grid[i-1][j] > grid[i][j-1]:
                    grid[i][j] += grid[i][j-1]
                
                else:
                    grid[i][j] += grid[i-1][j]
        return grid[i][j]