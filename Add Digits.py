class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        return (num - 1) % 9 + 1


s = Solution()
assert s.addDigits(0) == 0
assert s.addDigits(9) == 9
assert s.addDigits(22) == 4
assert s.addDigits(38) == 2
assert s.addDigits(44) == 8
assert s.addDigits(999) == 9
