class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = []
        visited = set()

        def getIsland(row: int, col: int, island: set[tuple[int, int]]): 
            if (col < 0 or col >= len(grid[0]) or
                row < 0 or row >= len(grid) or 
                (row, col) in island):
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
                if ((row, col) in visited or
                    grid[row][col] == "0"):
                    continue

                isInIsland = False
                for island in islands:
                    if (row, col) in island:
                        isInIsland = True
                        break

                if not isInIsland:
                    island = set()
                    getIsland(row, col, island)
                    islands.append(island)

        return len(islands)