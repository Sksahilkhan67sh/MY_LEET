from collections import deque
from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        directions = [
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1)
        ]

        connections = {
            1: {1, 3},      # left <-> right
            2: {0, 2},      # up <-> down
            3: {3, 2},      # left <-> down
            4: {1, 2},      # right <-> down
            5: {3, 0},      # left <-> up
            6: {1, 0}       # right <-> up
        }

        q = deque([(0, 0)])
        visited = {(0, 0)}

        while q:
            r, c = q.popleft()

            if r == m - 1 and c == n - 1:
                return True

            current_type = grid[r][c]

            for d, (dr, dc) in enumerate(directions):
                # Current street must connect in this direction
                if d not in connections[current_type]:
                    continue

                nr = r + dr
                nc = c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                if (nr, nc) in visited:
                    continue

                # Opposite direction in the neighbor
                opposite = (d + 2) % 4

                if opposite not in connections[grid[nr][nc]]:
                    continue

                visited.add((nr, nc))
                q.append((nr, nc))

        return False