class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(k):
            if k == 1:
                return (1, 1)
            if k == 2:
                return (1, 2)
            last = helper(k-1)
            return (last[1], sum(last))

        return helper(n)[1]

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.cache = dict()
        return self.recursion(n)

    def recursion(self, n):
        if n in self.cache:
            return self.cache[n]
        if n <= 2:
            return n
        ans = self.recursion(n-1) + self.recursion(n-2)
        self.cache[n] = ans
        return ans


s = Solution()
print(s.climbStairs(35))
