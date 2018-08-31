class Solution:
    def trap(self, height):
        left, right = 0, len(height)-1
        res = max_left = max_right = 0
        while left < right:
            max_left = max(max_left, height[left])
            max_right = max(max_right, height[right])
            if max_left > max_right:
                res += max_right - height[right]
                right -= 1
            else:
                res += max_left - height[left]
                left += 1
        return res


s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
