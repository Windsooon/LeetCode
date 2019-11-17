class Solution:
    # use direct to control index value
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        direct, index = False, 0
        lst = [''] * numRows
        for i in range(len(s)):
            if index == 0 or index >= numRows-1:
                direct = not direct
            lst[index] += s[i]
            if direct:
                index += 1
            else:
                index -= 1
        return ''.join(lst)


s = Solution()
print(s.convert('PAYPALISHIRING', 2))
