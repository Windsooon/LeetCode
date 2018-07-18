class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        matrix = [[0] * (m+1) for i in range((n+1))]
        matrix[0][0] = 0
        for i in range(1, n+1):
            matrix[i][0] = i
        for i in range(1, m+1):
            matrix[0][i] = i
        for k in range(1, m+1):
            for v in range(1, n+1):
                if word1[k-1] == word2[v-1]:
                    matrix[v][k] = matrix[v-1][k-1]
                else:
                    matrix[v][k] = min(
                        matrix[v-1][k]+1, matrix[v][k-1]+1, matrix[v-1][k-1]+1)
        return matrix[-1][-1]


s = Solution()
print(s.minDistance('abc', 'efgh'))
