class Solution(object):
    def convert(self, s, numRows):
        """
        not by myself
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        rows = [''] * numRows
        num = (numRows-1)*2
        for i, item in enumerate(s):
            if i % num >= numRows:
                rows[(num - i % num) % numRows] += item
            else:
                rows[i % num] += item
        return ''.join(rows)
