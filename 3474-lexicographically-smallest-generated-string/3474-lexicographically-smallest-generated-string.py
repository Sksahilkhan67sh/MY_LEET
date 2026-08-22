class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        length = n + m - 1

        ans = [None] * length
        fixed = [False] * length

        # Step 1: Apply all 'T' constraints
        for i in range(n):
            if str1[i] != 'T':
                continue

            for j in range(m):
                pos = i + j

                if ans[pos] is not None and ans[pos] != str2[j]:
                    return ""

                ans[pos] = str2[j]
                fixed[pos] = True

        # Step 2: Fill all remaining positions with 'a'
        for i in range(length):
            if ans[i] is None:
                ans[i] = 'a'

        # Step 3: Handle 'F' constraints
        for i in range(n):
            if str1[i] != 'F':
                continue

            # Check whether current substring equals str2
            same = True

            for j in range(m):
                if ans[i + j] != str2[j]:
                    same = False
                    break

            if not same:
                continue

            # Need to break this match.
            # Choose the rightmost unfixed position.
            changed = False

            for j in range(m - 1, -1, -1):
                pos = i + j

                if not fixed[pos]:
                    ans[pos] = 'b'
                    fixed[pos] = True
                    changed = True
                    break

            if not changed:
                return ""

        return ''.join(ans)