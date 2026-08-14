from typing import List

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat[0])
        k %= n

        for i in range(len(mat)):
            for j in range(n):
                if i % 2 == 0:
                    # Even row: shifted left
                    if mat[i][j] != mat[i][(j + k) % n]:
                        return False
                else:
                    # Odd row: shifted right
                    if mat[i][j] != mat[i][(j - k + n) % n]:
                        return False

        return True