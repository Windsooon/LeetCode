class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        lst = [0] * len(prices)
        for _ in range(2):
            # [3, 3, 5, 0, 0, 3, 1, 4]
            old = lst[:]
            max_profit = float('-inf')
            for i in range(1, len(lst)):
                max_profit = max(max_profit, old[i-1] - prices[i-1])
                lst[i] = max(lst[i-1], prices[i] + max_profit)
        return lst[-1]


s = Solution()
print(s.maxProfit([1,2]))
print(s.maxProfit([3,3,5,0,0,3,1,4]))
# print(s.maxProfit([0,3,1,4]))
# print(s.maxProfit([7,6,4,3,1]))
# print(s.maxProfit([1,2,4,2,5,7,2,4,9,0]))
