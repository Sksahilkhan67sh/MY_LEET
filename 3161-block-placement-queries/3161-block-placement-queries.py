from typing import List
from bisect import bisect_right


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:

        # Coordinate compression of all possible obstacles
        coords = {0}

        for q in queries:
            if q[0] == 1:
                coords.add(q[1])

        max_x = max(q[1] for q in queries)
        coords.add(max_x + 1)  # sentinel

        coords = sorted(coords)
        n = len(coords)

        index = {x: i for i, x in enumerate(coords)}

        # -------------------------------------------------
        # DSU for previous active obstacle
        # DSU for next active obstacle
        # -------------------------------------------------

        prev = list(range(n))
        nxt = list(range(n))

        def find_prev(x):
            while prev[x] != x:
                prev[x] = prev[prev[x]]
                x = prev[x]
            return x

        def find_next(x):
            while nxt[x] != x:
                nxt[x] = nxt[nxt[x]]
                x = nxt[x]
            return x

        # -------------------------------------------------
        # Fenwick Tree for maximum gap
        # -------------------------------------------------

        bit = [0] * (n + 1)

        def update(i, value):
            i += 1
            while i <= n:
                bit[i] = max(bit[i], value)
                i += i & -i

        def query(i):
            # Maximum gap in [0 ... i]
            i += 1
            ans = 0

            while i > 0:
                ans = max(ans, bit[i])
                i -= i & -i

            return ans

        # Initially every possible type-1 position is an obstacle.
        # Store gap ending at every obstacle.
        for i in range(1, n):
            update(i, coords[i] - coords[i - 1])

        result = []

        # -------------------------------------------------
        # Process backwards
        # -------------------------------------------------

        for q in reversed(queries):

            x = q[1]

            # Type 1: remove obstacle x
            if q[0] == 1:

                i = index[x]

                left = find_prev(i - 1)
                right = find_next(i + 1)

                # Removing x merges:
                #
                # left ---- x ---- right
                #
                # into:
                #
                # left ----------- right

                update(
                    right,
                    coords[right] - coords[left]
                )

                # Remove x from both DSU structures
                prev[i] = left
                nxt[i] = right

            # Type 2
            else:

                sz = q[2]

                # Rightmost coordinate <= x
                pos = bisect_right(coords, x) - 1

                # Actual active obstacle <= x
                p = find_prev(pos)

                # Largest complete gap ending before p
                best_gap = query(p)

                # Gap from last obstacle to x
                best_gap = max(
                    best_gap,
                    x - coords[p]
                )

                result.append(best_gap >= sz)

        result.reverse()

        return result