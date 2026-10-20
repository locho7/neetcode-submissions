class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0

        def getIsland(row: int, col: int): 
            if (col < 0 or col >= len(grid[0]) or
                row < 0 or row >= len(grid) or 
                (row, col) in visited):
                return
            
            visited.add((row, col))
            if grid[row][col] == "0":
                return
            for r in [row - 1, row + 1]:
                getIsland(r, col)
            for c in [col - 1, col + 1]:
                getIsland(row, c)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if ((row, col) not in visited and
                    grid[row][col] == "1"):
                    getIsland(row, col)
                    islands += 1

        return islands