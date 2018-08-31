class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # build up matrix
        matrix = [[0] * (len(s)+1) for _ in range(len(p)+1)]
        lst = []
        for index in range(len(matrix)-1):
            if p[index] == '*' and lst.count('*') == len(lst):
                matrix[index+1][0] = 1
            lst.append(p[index])
        matrix[0][0] = 1
        # [[1, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 0], [0, 1, 1, 1], [0, 0, 0, 1]]
        for row_index in range(1, len(p)+1):
            for column_index in range(1, len(s)+1):
                if matrix[row_index-1][column_index-1]:
                    if p[row_index-1] == '*' or p[row_index-1] == '?' or p[row_index-1] == s[column_index-1]:
                        matrix[row_index][column_index] = 1
                else:
                    if p[row_index-1] == '*' and (matrix[row_index-1][column_index] or matrix[row_index][column_index-1]):
                        matrix[row_index][column_index] = 1
        # print(matrix)
        return matrix[-1][-1] == True


s = Solution()
assert s.isMatch('adceb', '*a*b') == True
assert s.isMatch('acdcb', 'a*c?b') == False
assert s.isMatch('cd', '?a') == False
assert s.isMatch('aa', '*') == True
assert s.isMatch('aa', 'a') == False
assert s.isMatch('aab', 'c*a*b') == False
assert s.isMatch('ho', '**ho') == True
