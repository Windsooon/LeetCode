class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n:
            k = n % 3
            if k != 0 and n != 1:
                return False
            n = n//3
        return True

s = Solution()
print(s.isPowerOfThree(19684))
print(s.isPowerOfThree(27))
