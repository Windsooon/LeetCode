class Solution:
    def largestRectangleArea(self, height):
        height.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        height.pop()
        return ans


s = Solution()
# assert (s.largestRectangleArea([2, 1, 5, 6, 2, 3])) == 10
# assert (s.largestRectangleArea([0, 9])) == 9
print(s.largestRectangleArea([2, 1, 2]))
