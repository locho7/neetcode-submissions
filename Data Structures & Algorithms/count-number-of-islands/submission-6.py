class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0

        def getIsland(row: int, col: int, island: set[tuple[int, int]]): 
            if (col < 0 or col >= len(grid[0]) or
                row < 0 or row >= len(grid) or 
                (row, col) in visited):
                return
            
            visited.add((row, col))
            if grid[row][col] == "0":
                return

            island.add((row, col))
            for r in [row - 1, row + 1]:
                getIsland(r, col, island)
            for c in [col - 1, col + 1]:
                getIsland(row, c, island)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if ((row, col) not in visited and
                    grid[row][col] == "1"):
                    getIsland(row, col, set())
                    islands += 1

        return islands