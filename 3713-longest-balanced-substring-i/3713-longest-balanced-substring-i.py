from collections import Counter

class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            cnt = Counter()
            mx = v = 0
            for j in range(i, n):
                cnt[s[j]] += 1
                if cnt[s[j]] == 1:
                    v += 1
                mx = max(mx, cnt[s[j]])
                if mx * v == j - i + 1:
                    ans = max(ans, j - i + 1)
        return ans