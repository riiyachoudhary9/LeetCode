class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0

        while x:
            rev = rev * 10 + x % 10
            x //= 10

        rev *= sign
        return rev if -2**31 <= rev <= 2**31 - 1 else 0