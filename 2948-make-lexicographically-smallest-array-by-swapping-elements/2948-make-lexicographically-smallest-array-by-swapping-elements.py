from typing import List

class Solution:
    def lexicographicallySmallestArray(
        self,
        nums: List[int],
        limit: int
    ) -> List[int]:

        n = len(nums)

        # (value, original_index)
        arr = sorted((nums[i], i) for i in range(n))

        ans = [0] * n

        i = 0

        while i < n:
            j = i + 1

            # Find one connected/swappable group
            while (
                j < n
                and arr[j][0] - arr[j - 1][0] <= limit
            ):
                j += 1

            # Original indices of this group
            indices = sorted(arr[k][1] for k in range(i, j))

            # Values are already sorted because arr is sorted
            for p in range(j - i):
                ans[indices[p]] = arr[i + p][0]

            i = j

        return ans