class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        
        m = len(grid)
        n = len(grid[0])

        visited = [[False] * n for _ in range(m)]

        directions = [
            (1, 0),   # down
            (-1, 0),  # up
            (0, 1),   # right
            (0, -1)   # left
        ]

        count = 0

        def dfs(r, c):
            # Mark current cell visited
            visited[r][c] = True

            # Add current cell's value
            total = grid[r][c]

            # Explore 4 directions
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < m and
                    0 <= nc < n and
                    grid[nr][nc] > 0 and
                    not visited[nr][nc]
                ):
                    total += dfs(nr, nc)

            return total

        for r in range(m):
            for c in range(n):

                # Found a new island
                if grid[r][c] > 0 and not visited[r][c]:

                    island_sum = dfs(r, c)

                    if island_sum % k == 0:
                        count += 1

        return count