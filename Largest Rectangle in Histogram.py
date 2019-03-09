class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_area = 0
        heights.append(0)
        stack = [-1]
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                cur_height = heights[stack.pop()]
                cur_width = i - stack[-1] - 1
                max_area = max(max_area, cur_width * cur_height)
            stack.append(i)
        return max_area
