class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        elif n < 0:
            n = -n
            x = 1/x
        pow = x
        while n > 1:
            pow *= x
            n -= 1
        return pow

b = Solution()
print(b.myPow(8.88023, 3))
