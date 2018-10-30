class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        after = self.helper(matrix)
        max_val = 0
        for a in after:
            max_val = max(max_val, self.max_re(a))
        return max_val

    def max_re(self, lst):
        max_area = 0
        lst.append('0')
        stack = [-1]
        for i in range(len(lst)):
            while int(lst[i]) < int(lst[stack[-1]]):
                height = int(lst[stack.pop()])
                width = i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        return max_area

    def helper(self, matrix):
        pre = matrix[0]
        after = [pre]
        for i in range(1, len(matrix)):
            cur = []
            for j in range(len(pre)):
                if matrix[i][j] == '0':
                    cur.append(str(0))
                else:
                    cur.append(str(1+int(pre[j])))
            after.append(cur)
            pre = cur
        return after


s = Solution()

matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
print(s.maximalRectangle(matrix))
