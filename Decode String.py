class Solution(object):
    def decodeString(self, s):
        stack = [['', 1]]
        num = ''
        for ele in s:
            if ele.isdigit():
                num += ele
            elif ele == '[':
                stack.append(['', int(num)])
                num = ''
            elif ele == ']':
                top = stack.pop()
                stack[-1][0] += top[0] * top[1]
            else:
                stack[-1][0] += ele
        return stack[0][0]


s = Solution()
print(s.decodeString('3[a]2[bc]'))
print(s.decodeString('3[a2[c]]'))
print(s.decodeString('2[abc]3[cd]ef'))
