class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_cur, ans = 0, 0
        for p in range(1, len(prices)):
            max_cur += prices[p] - prices[p-1]
            max_cur = max(0, max_cur)
            print(max_cur)
            ans = max(ans, max_cur)
        return ans


s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
