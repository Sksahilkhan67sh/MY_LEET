from typing import List
from bisect import bisect_left


class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        perimeter = 4 * side

        # Map every boundary point to its position on the perimeter.
        arr = []

        for x, y in points:
            if x == 0:
                pos = y
            elif y == side:
                pos = side + x
            elif x == side:
                pos = 3 * side - y
            else:
                pos = 4 * side - x

            arr.append(pos)

        arr.sort()
        n = len(arr)

        # Duplicate the circle so we can handle wrap-around.
        a = arr + [x + perimeter for x in arr]

        def can(d: int) -> bool:
            # Try every point as the first selected point.
            for start in range(n):
                first = a[start]
                limit = first + perimeter - d

                cur = start

                # Greedily choose the next point at least d away.
                for _ in range(k - 1):
                    nxt = bisect_left(a, a[cur] + d, cur + 1)

                    if nxt >= start + n:
                        break

                    cur = nxt

                else:
                    # Need the final selected point to be at least d
                    # away from the starting point around the circle.
                    if a[cur] <= limit:
                        return True

            return False

        # The answer can never exceed side.
        lo = 0
        hi = side

        while lo < hi:
            mid = (lo + hi + 1) // 2

            if can(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo