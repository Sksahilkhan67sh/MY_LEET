class Solution:
    def mirrorDistance(self, n: int) -> int:
        original = n
        rev = 0

        while n > 0:
            digit = n % 10
            rev = rev * 10 + digit
            n //= 10

        return abs(original - rev)