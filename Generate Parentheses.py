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

a = Solution()
print(a.generateParenthesis(3))
