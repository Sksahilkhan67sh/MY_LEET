class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = []

        def dfs(cur):
            if len(ans) == k:
                return

            if len(cur) == n:
                ans.append(cur)
                return

            for ch in "abc":
                if not cur or cur[-1] != ch:
                    dfs(cur + ch)

        dfs("")
        return ans[k - 1] if k <= len(ans) else ""