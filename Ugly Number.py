class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        while num % 5 == 0:
            num = num//5
        while num % 3 == 0:
            num = num//3
        while num % 2 == 0:
            num = num//2
        if num != 1:
            return False
        return True


s = Solution()
assert s.isUgly(30) is True
assert s.isUgly(8) is True
assert s.isUgly(28) is False
assert s.isUgly(14) is False
