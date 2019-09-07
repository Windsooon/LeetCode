class Solution:
    def trap(self, height):
        if not height:
            return 0
        ans = 0
        stack = []
        left = self.helper(height)
        stack.append(0)
        for i in range(1, len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if left[top] != -1:
                    ans += max(0, min(height[i], height[left[top]])-height[top]) * (i-left[top]-1)
            stack.append(i)
        return ans

    def helper(self, height):
        index = [-1] * len(height)
        stack = [0]
        for i in range(1, len(height)):
            while stack:
                if height[i] <= height[stack[-1]]:
                    index[i] = stack[-1]
                    break
                else:
                    stack.pop()
            stack.append(i)
        return index

s = Solution()
print(s.trap([4, 2, 3]))
# print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
