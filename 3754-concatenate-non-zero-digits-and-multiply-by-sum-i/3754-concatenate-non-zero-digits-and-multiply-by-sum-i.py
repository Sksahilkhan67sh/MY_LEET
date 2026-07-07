class Solution:
    def sumAndMultiply(self, n: int) -> int:

        x = 0
        s = 0
        p = 1

        while n > 0:

            digit = n % 10

            if digit != 0:
                x += digit * p
                s += digit
                p *= 10

            n //= 10

        return x * s