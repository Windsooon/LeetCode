class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # [0, 0, 0]
        ans = [0] * (rowIndex+1)
        # [1, 0, 0]
        ans[0] = 1
        # rowIndex = 3
        for i in range(rowIndex+1):
            # 0, 1, 2
            for j in range(i, 0, -1):
                ans[j] += ans[j-1]
        return ans


s = Solution()
print(s.getRow(3))
