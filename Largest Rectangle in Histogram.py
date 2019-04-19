class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        max_area = 0
        heights.insert(0, 0)
        heights.append(0)
        stack = [0]
        max_area = 0
        # 0, 2, 1, 1, 1, 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                cur_height = heights[stack.pop()]
                cur_width = i - stack[-1] - 1
                max_area = max(max_area, cur_height * cur_width)
            stack.append(i)
        return max_area
        

s = Solution()
print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))
