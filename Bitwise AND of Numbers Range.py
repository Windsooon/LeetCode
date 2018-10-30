class Solution:
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == n:
            return m
        answer = m
        for i in range(m+1, n+1):
            answer = answer & i
        return answer


