from typing import List

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        visited = [[False] * n for _ in range(m)]

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        def dfs(r, c, pr, pc):
            visited[r][c] = True

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                # Different character
                if grid[nr][nc] != grid[r][c]:
                    continue

                # Don't go directly back to parent
                if nr == pr and nc == pc:
                    continue

                # Already visited same-character cell => cycle
                if visited[nr][nc]:
                    return True

                if dfs(nr, nc, r, c):
                    return True

            return False

        for r in range(m):
            for c in range(n):
                if not visited[r][c]:
                    if dfs(r, c, -1, -1):
                        return True

        return False