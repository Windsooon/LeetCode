class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        stack = []
        if len(s) == 1:
            return False

        for i in s:
            if i in d.keys():
                stack.append(i)
            elif stack == [] or i != d[stack.pop()]:
                return False
        return stack == []

a = Solution()
print(a.isValid("(("))
