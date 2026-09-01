from collections import deque
from typing import List


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])

        lumetarkon = classroom

        # Number every litter cell
        litter_id = {}
        sr = sc = 0
        k = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    sr, sc = r, c
                elif classroom[r][c] == 'L':
                    litter_id[(r, c)] = k
                    k += 1

        if k == 0:
            return 0

        full_mask = (1 << k) - 1

        # best[r][c][mask] = maximum energy we've had
        # at (r,c) after collecting the same litter.
        best = [
            [[-1] * (1 << k) for _ in range(n)]
            for _ in range(m)
        ]

        q = deque()
        q.append((sr, sc, energy, full_mask))
        best[sr][sc][full_mask] = energy

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        moves = 0

        while q:
            for _ in range(len(q)):
                r, c, e, mask = q.popleft()

                if mask == 0:
                    return moves

                # No energy -> cannot make another move
                if e == 0:
                    continue

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if not (0 <= nr < m and 0 <= nc < n):
                        continue

                    if classroom[nr][nc] == 'X':
                        continue

                    # Every move costs 1 energy
                    ne = e - 1

                    # Reset after entering R
                    if classroom[nr][nc] == 'R':
                        ne = energy

                    nmask = mask

                    # Collect litter
                    if classroom[nr][nc] == 'L':
                        bit = litter_id[(nr, nc)]
                        nmask &= ~(1 << bit)

                    # If we've already reached this state with
                    # equal or more energy, this state is useless.
                    if ne <= best[nr][nc][nmask]:
                        continue

                    best[nr][nc][nmask] = ne
                    q.append((nr, nc, ne, nmask))

            moves += 1

        return -1