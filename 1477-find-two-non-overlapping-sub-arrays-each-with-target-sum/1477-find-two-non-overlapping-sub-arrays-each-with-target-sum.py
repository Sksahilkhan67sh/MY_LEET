from typing import List

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        INF = n + 1

        # best[i] = minimum length of a valid subarray
        # completely inside arr[0:i]
        best = [INF] * (n + 1)

        ans = INF

        left = 0
        current_sum = 0

        for right in range(n):
            current_sum += arr[right]

            while left <= right and current_sum > target:
                current_sum -= arr[left]
                left += 1

            if current_sum == target:
                length = right - left + 1

                # Combine with a previous non-overlapping subarray
                if best[left] != INF:
                    ans = min(ans, length + best[left])

                # Best valid subarray using positions <= right
                best[right + 1] = min(best[right], length)
            else:
                best[right + 1] = best[right]

        return -1 if ans == INF else ans