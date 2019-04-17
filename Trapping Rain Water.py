class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack, result = [], 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                bot = stack.pop()
                result += 0 if not stack else (min(height[i], height[stack[-1]]) - height[bot]) * (i-stack[-1]-1)
            stack.append(i)
        return result

s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
