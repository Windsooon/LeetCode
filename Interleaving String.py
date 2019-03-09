class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s3) != len(s1) + len(s2):
            return False
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        dp = [True] * (len(s1)+1)
        for d in range(1, len(s1)+1):
            dp[d] = dp[d-1] and s1[d-1] == s3[d-1]
        for s2_i in range(1, len(s2)+1):
            dp[0] = (dp[0] and s2[s2_i-1] == s3[s2_i-1])
            for s1_i in range(1, len(s1)+1):
                dp[s1_i] = (dp[s1_i-1] and s1[s1_i-1] == s3[s1_i+s2_i-1]) | \
                    dp[s1_i] and s2[s2_i-1] == s3[s1_i+s2_i-1]
        print(dp)
        return dp[-1]


s = Solution()
s1 = 'aabcc'
s2 = 'dbbca'
s3 = 'aadbbcbcac'
print(s.isInterleave(s1, s2, s3))
