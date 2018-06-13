class Solution:
    def generate(self, numRows):
        ans = [1]
        # 1, 2, 1
        for i in range(numRows):
            # 2
            for j in range(len(ans)-1):
                ans = ans.append(ans[j] + ans[j+1]  


s = Solution()
print(s.generate(5))
