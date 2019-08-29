class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []

        def helper(matrix, result):
            if not matrix:
                return
            result += matrix.pop(0)
            helper(list(zip(*matrix))[::-1], result)
        helper(matrix, result)
        return result

s = Solution()
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(s.spiralOrder(a))
