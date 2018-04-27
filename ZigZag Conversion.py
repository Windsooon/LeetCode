class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        stack_lst = [''] * numRows
        i = 0
        for k, v in enumerate(s):
            stack_lst[i] += v
            if i == 0:
                min = True
                i += 1
            elif i < numRows-1:
                if min:
                    i += 1
                else:
                    i -= 1
            elif i == numRows-1:
                min = False
                i -= 1
        return ''.join(stack_lst)


s = Solution()
print(s.convert('AB', 1))
