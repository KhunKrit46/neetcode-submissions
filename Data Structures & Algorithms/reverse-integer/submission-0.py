class Solution:
    def reverse(self, x: int) -> int:
        new = ''
        if x < 0:
            new = '-'
            x *= -1
        for num in str(x)[::-1]:
            new += num
        if -2**31 <= int(new) <= 2**31 - 1:
            return int(new)
        return 0