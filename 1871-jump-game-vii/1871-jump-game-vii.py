class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)

        dp = [False] * n
        dp[0] = True

        reachable = 0

        for i in range(1, n):

            # Add the position that has just entered
            # the valid jump window.
            if i - minJump >= 0 and dp[i - minJump]:
                reachable += 1

            # Remove the position that is now too far away.
            if i - maxJump - 1 >= 0 and dp[i - maxJump - 1]:
                reachable -= 1

            # i is reachable if there is at least one
            # reachable position in [i-maxJump, i-minJump]
            if s[i] == '0' and reachable > 0:
                dp[i] = True

        return dp[n - 1]