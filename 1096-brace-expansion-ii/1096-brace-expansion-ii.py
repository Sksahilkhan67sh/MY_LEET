from typing import List

class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        result = set()

        def dfs(exp):
            # Find the first closing brace
            right = exp.find('}')

            # No braces left -> fully expanded string
            if right == -1:
                result.add(exp)
                return

            # Find matching innermost opening brace
            left = exp.rfind('{', 0, right)

            prefix = exp[:left]
            suffix = exp[right + 1:]

            # Innermost brace has no nested braces,
            # so we can split by comma
            options = exp[left + 1:right].split(',')

            for option in options:
                dfs(prefix + option + suffix)

        dfs(expression)

        return sorted(result)