class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        f = [[0] * (k + 1) for _ in range(n + 1)]
        g = [[0] * (k + 1) for _ in range(n + 1)]

        f[1][0] = 1

        for i in range(2, n + 1):
            for j in range(k + 1):

                # Don't end a segment here
                f[i][j] = (f[i - 1][j] + g[i - 1][j]) % MOD

                # Continue existing possibilities
                g[i][j] = g[i - 1][j]

                if j > 0:
                    # Start a new segment
                    g[i][j] += f[i - 1][j - 1]
                    g[i][j] %= MOD

                    # End one segment and potentially start/share endpoint
                    g[i][j] += g[i - 1][j - 1]
                    g[i][j] %= MOD

        return (f[n][k] + g[n][k]) % MOD