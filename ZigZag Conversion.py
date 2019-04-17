# class Solution(object):
#     def convert(self, s, numRows):
#         """
#         :type s: str
#         :type numRows: int
#         :rtype: str
#         """
#         stack_lst = [''] * numRows
#         i = 0
#         for k, v in enumerate(s):
#             stack_lst[i] += v
#             if i == 0:
#                 min = True
#                 i += 1
#             elif i < numRows-1:
#                 if min:
#                     i += 1
#                 else:
#                     i -= 1
#             elif i == numRows-1:
#                 min = False
#                 i -= 1
#         return ''.join(stack_lst)


class Solution:
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
