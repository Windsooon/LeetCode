class Solution(object):
    def generateParenthesis(self, n):
        def helper(p, left, right, answer=[]):
            if left:
                helper(p + '(', left-1, right)
            if right > left:
                helper(p + ')', left, right-1)
            if not right:
                answer.append(p)
            return answer
        return helper('', n, n)

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        breakpoint()
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                for x in dp[j]:
                    for y in dp[i-j-1]:
                        dp[i] += ['(' + x + ')' + y]
        return dp[n]

a = Solution()
print(a.generateParenthesis(3))
