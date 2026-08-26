from typing import List

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        m = 2 * n

        # d[i] = closest distance to another equal value
        d = [m] * m

        # Find closest equal element on the left
        last = {}

        for i in range(m):
            x = nums[i % n]

            if x in last:
                d[i] = min(d[i], i - last[x])

            last[x] = i

        # Find closest equal element on the right
        last = {}

        for i in range(m - 1, -1, -1):
            x = nums[i % n]

            if x in last:
                d[i] = min(d[i], last[x] - i)

            last[x] = i

        # Combine the two copies
        for i in range(n):
            d[i] = min(d[i], d[i + n])

        # Answer queries
        ans = []

        for q in queries:
            if d[q] >= n:
                ans.append(-1)
            else:
                ans.append(d[q])

        return ans