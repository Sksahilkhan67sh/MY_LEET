from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        for _ in range(4):
            if mat == target:
                return True

            # Rotate 90 degrees clockwise
            mat = [
                [mat[n - 1 - j][i] for j in range(n)]
                for i in range(n)
            ]

        return False