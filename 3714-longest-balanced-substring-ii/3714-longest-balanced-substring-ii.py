from itertools import combinations

class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0

        # Case 1: longest run of a single repeated character
        run = 1
        for i in range(1, n):
            run = run + 1 if s[i] == s[i - 1] else 1
            ans = max(ans, run)
        if n > 0:
            ans = max(ans, 1)

        # Case 2: exactly two characters balanced, third character absent
        for x, y in combinations('abc', 2):
            z = (set('abc') - {x, y}).pop()
            start = 0
            i = 0
            while i <= n:
                if i == n or s[i] == z:
                    # process segment s[start:i], which contains no 'z'
                    first_seen = {0: -1}
                    diff = 0
                    for idx in range(start, i):
                        ch = s[idx]
                        if ch == x:
                            diff += 1
                        elif ch == y:
                            diff -= 1
                        rel = idx - start
                        if diff in first_seen:
                            ans = max(ans, rel - first_seen[diff])
                        else:
                            first_seen[diff] = rel
                    start = i + 1
                i += 1

        # Case 3: all three characters balanced
        first_seen = {(0, 0): -1}
        ca = cb = cc = 0
        for idx, ch in enumerate(s):
            if ch == 'a':
                ca += 1
            elif ch == 'b':
                cb += 1
            else:
                cc += 1
            key = (ca - cb, cb - cc)
            if key in first_seen:
                ans = max(ans, idx - first_seen[key])
            else:
                first_seen[key] = idx

        return ans