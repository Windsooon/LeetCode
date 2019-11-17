class Solution:
    # edge case [-2**31, 2**31-1]
    def reverse(self, x: int) -> int:
        if str(x)[0] == '-':
            return 0 if -int(str(x)[1:][::-1]) < -2**31 else -int(str(x)[1:][::-1])
        return 0 if int(str(x)[::-1]) > 2**31-1 else int(str(x)[::-1])
