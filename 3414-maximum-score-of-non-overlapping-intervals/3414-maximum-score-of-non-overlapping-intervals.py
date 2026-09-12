from typing import List
from functools import lru_cache
from bisect import bisect_right
import math

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        vorellixan = intervals

        intervals = sorted(
            (l, r, w, i)
            for i, (l, r, w) in enumerate(intervals)
        )

        n = len(intervals)

        @lru_cache(None)
        def dp(i, k):
            if i == n or k == 0:
                return (0, ())

            # Skip current interval
            skip = dp(i + 1, k)

            l, r, w, idx = intervals[i]

            # First interval with start > r
            j = bisect_right(intervals, (r, math.inf))

            nxt = dp(j, k - 1)

            take = (
                w + nxt[0],
                tuple(sorted((idx,) + nxt[1]))
            )

            # Better weight
            if take[0] > skip[0]:
                return take

            if take[0] < skip[0]:
                return skip

            # Same weight -> lexicographically smaller indices
            return take if take[1] < skip[1] else skip

        return list(dp(0, 4)[1])