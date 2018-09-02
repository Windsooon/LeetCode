class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # build up matrix
        matrix = [[False] * (len(p)+1) for _ in range(len(s)+1)]
        matrix[0][0] = True
        # [[1, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 0], [0, 1, 1, 1], [0, 0, 0, 1]]
        for row_i in range(len(s)+1):
            for column_i in range(1, len(p)+1):
                if p[column_i-1] == '*':
                    matrix[row_i][column_i] = matrix[row_i][column_i-1] or (row_i > 0 and matrix[row_i-1][column_i])
                elif row_i > 0 and (p[column_i-1] == '?' or p[column_i-1] == s[row_i-1]):
                    matrix[row_i][column_i] = matrix[row_i-1][column_i-1]
        return matrix[-1][-1]


s = Solution()
# assert s.isMatch('acdcb', 'a*c?b') is False
assert s.isMatch('adceb', '*a*b') is True
# assert s.isMatch('adceb', '*a*') is True
# assert s.isMatch('cd', '?a') is False
# assert s.isMatch('aa', '*') is True
# assert s.isMatch('aa', 'a') is False
# assert s.isMatch('a', '') is False
# assert s.isMatch('aab', 'c*a*b') is False
# assert s.isMatch('ho', '**ho') is True
