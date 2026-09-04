from collections import deque
from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = deque([start])
        visited = [False] * len(arr)
        visited[start] = True

        while q:
            i = q.popleft()

            if arr[i] == 0:
                return True

            jump = arr[i]

            # Jump left
            left = i - jump
            if left >= 0 and not visited[left]:
                visited[left] = True
                q.append(left)

            # Jump right
            right = i + jump
            if right < len(arr) and not visited[right]:
                visited[right] = True
                q.append(right)

        return False