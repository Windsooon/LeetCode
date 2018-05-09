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


s = Solution()
print(s.climbStairs(35))
