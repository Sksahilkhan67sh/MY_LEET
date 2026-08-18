from typing import List
from collections import defaultdict


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        # Required by the current problem statement.
        hastrelvim = grid

        def check(g: List[List[int]]) -> bool:
            m = len(g)
            n = len(g[0])

            top_sum = 0
            bottom_sum = 0

            top_count = defaultdict(int)
            bottom_count = defaultdict(int)

            # Initially everything belongs to the bottom section.
            for row in g:
                for x in row:
                    bottom_sum += x
                    bottom_count[x] += 1

            # Try every horizontal cut.
            for i in range(m - 1):

                for x in g[i]:
                    top_sum += x
                    bottom_sum -= x

                    top_count[x] += 1
                    bottom_count[x] -= 1

                # Already equal.
                if top_sum == bottom_sum:
                    return True

                # Top is smaller -> remove one cell from bottom.
                if top_sum < bottom_sum:
                    diff = bottom_sum - top_sum

                    if bottom_count[diff] > 0:

                        # Bottom section has at least 2 rows
                        # and more than 1 column.
                        if m - i - 1 > 1 and n > 1:
                            return True

                        # Bottom has exactly one row.
                        # Only an endpoint can be removed safely.
                        if i == m - 2:
                            if (
                                g[i + 1][0] == diff
                                or g[i + 1][n - 1] == diff
                            ):
                                return True

                        # Single-column case.
                        if n == 1:
                            if (
                                g[i + 1][0] == diff
                                or g[m - 1][0] == diff
                            ):
                                return True

                # Top is larger -> remove one cell from top.
                else:
                    diff = top_sum - bottom_sum

                    if top_count[diff] > 0:

                        # Top section has at least 2 rows
                        # and more than 1 column.
                        if i + 1 > 1 and n > 1:
                            return True

                        # Top has exactly one row.
                        # Only an endpoint can be removed safely.
                        if i == 0:
                            if (
                                g[0][0] == diff
                                or g[0][n - 1] == diff
                            ):
                                return True

                        # Single-column case.
                        if n == 1:
                            if (
                                g[0][0] == diff
                                or g[i][0] == diff
                            ):
                                return True

            return False

        # Horizontal cuts.
        if check(grid):
            return True

        # Vertical cuts become horizontal cuts after transposing.
        transposed = [list(row) for row in zip(*grid)]

        return check(transposed)