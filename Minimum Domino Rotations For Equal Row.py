class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        if len(A) < 2:
            return 0
        dp = [[0] * len(A) for i in range(2)]
        # dp[0][i] minimum to equal when not swap i
        # dp[1][i] minimum to equal when swap i
        # dp[0][i] = min(dp[0][i-1], dp[1][i-1]) if A[i] == A[i-1]
        #          = dp[1][i-1]                  else
        # dp[1][i] = 1 + dp[1][i-1] if A[i] == A[i-1]
        #          = 1 + dp[0][i-1]
        dp[1][0] = 1
        for i in range(1, len(A)):
            if A[i] != A[i-1] and A[i] != B[i-1] and A[i-1] != B[i] and B[i] != B[i-1]:
                return -1
            if A[i] == A[i-1] or B[i] == B[i-1]:
                dp[0][i] = dp[0][i-1]
                dp[1][i] = 1 + dp[1][i-1]
            else:
                dp[0][i] = dp[1][i-1]
                dp[1][i] = 1 + dp[0][i-1]
        return min(dp[0][-1], dp[1][-1])

s = Solution()
print(s.minDominoRotations([1,2,3,4,6], [6,6,6,6,5]))
