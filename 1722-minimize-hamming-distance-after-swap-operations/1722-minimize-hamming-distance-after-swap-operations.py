from collections import defaultdict, Counter
from typing import List

class Solution:
    def minimumHammingDistance(
        self,
        source: List[int],
        target: List[int],
        allowedSwaps: List[List[int]]
    ) -> int:

        n = len(source)
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            ra = find(a)
            rb = find(b)

            if ra != rb:
                parent[ra] = rb

        # Build connected components
        for a, b in allowedSwaps:
            union(a, b)

        # Count values available in each component
        count = defaultdict(Counter)

        for i in range(n):
            root = find(i)
            count[root][source[i]] += 1

        # Match target values with available source values
        ans = 0

        for i in range(n):
            root = find(i)
            value = target[i]

            if count[root][value] > 0:
                count[root][value] -= 1
            else:
                ans += 1

        return ans