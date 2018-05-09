class Solution:
    def generate(self, numRows):
        ans = [[1] * (i+1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(1, i):
                ans[i][j] = ans[i-1][j-1] + ans[i-1][j]
        return ans


s = Solution()
print(s.generate(5))
