class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [""]
        
        for ch in s:
            if ch == '(':
                stack.append("")
            
            elif ch == ')':
                current = stack.pop()
                stack[-1] += current[::-1]
            
            else:
                stack[-1] += ch
        
        return stack[0]