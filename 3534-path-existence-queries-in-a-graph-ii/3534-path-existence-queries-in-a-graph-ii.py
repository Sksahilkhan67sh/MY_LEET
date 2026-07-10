from typing import List
from functools import lru_cache
import bisect

class DSU:
    def __init__(self, n: int):
        self.root = list(range(n))
    
    def find(self, x: int) -> int:
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x: int, y: int):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.root[rx] = ry

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # Sort nodes by value
        nodes = sorted([(x, i) for i, x in enumerate(nums)])
        values = [v for v, _ in nodes]
        idx_map = [i for _, i in nodes]  # nodes[i].original_index

        # Build DSU over adjacent nodes if within maxDiff
        dsu = DSU(n)
        for i in range(n - 1):
            if values[i+1] - values[i] <= maxDiff:
                u, v = idx_map[i], idx_map[i+1]
                dsu.union(u, v)

        # Precompute for each i the farthest index nxt[i] such that
        # values[nxt[i]] <= values[i] + maxDiff
        nxt = [0] * n
        for i in range(n):
            limit = values[i] + maxDiff
            # bisect_right returns insertion point after all <= limit
            pos = bisect.bisect_right(values, limit) - 1
            nxt[i] = pos

        # Memoized function: dist from sorted index i to sorted index j
        @lru_cache(None)
        def _dist(i: int, j: int) -> int:
            if i >= j:
                return 0
            # one jump from i to nxt[i]
            return 1 + _dist(nxt[i], j)

        def query(u: int, v: int) -> int:
            if dsu.find(u) != dsu.find(v):
                return -1
            if u == v:
                return 0
            if nums[u] == nums[v]:
                return 1
            # Ensure we always go from smaller value to larger
            if nums[u] > nums[v]:
                return query(v, u)
            # Find sorted indices
            i = bisect.bisect_left(values, nums[u], 0, n)
            # Because values are sorted and may have duplicates, we need the exact position
            # Adjust i to point to the node with original index u
            while i < n and idx_map[i] != u:
                i += 1
            j = bisect.bisect_left(values, nums[v], 0, n)
            while j < n and idx_map[j] != v:
                j += 1
            return _dist(i, j)

        return [query(u, v) for u, v in queries]