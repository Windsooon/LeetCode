class Solution:
    def removeDuplicates(self, S):
        stack = []
        for i in range(len(S)):
            if stack and stack[-1] == S[i]:
                stack.pop()
            else:
                stack.append(S[i])
        return ''.join(stack)

s = Solution()
S = "abbaca"
print(s.removeDuplicates(S))
