class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        # base setup
        for m in matrix:
            m.insert(0, '0')
            m.append("0")
        stack = [0]
        cur = [0] * len(matrix[0])
        max_area = 0
        for m in matrix:
            for i in range(len(m)):
                if m[i] == '1':
                    cur[i] = cur[i] + 1
                else:
                    cur[i] = 0
                while stack and cur[stack[-1]] > cur[i]:
                    cur_height = cur[stack.pop()]
                    cur_width = i - stack[-1] - 1
                    max_area = max(max_area, cur_height * cur_width)
                stack.append(i)
        return max_area

s = Solution()

matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]

matrix = [["1"]]
print(s.maximalRectangle(matrix))
