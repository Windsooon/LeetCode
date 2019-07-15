class Solution(object):
    def removeDuplicateLetters(self, s):
        stack = []
        count = [0] * 26
        for ele in s:
            # bab
            # [1, 2]
            count[ord(ele)-ord('a')] += 1
        visited = [False] * 26
        breakpoint()
        for ele in s:
            # [0, 0]
            count[ord(ele)-ord('a')] -= 1
            if visited[ord(ele)-ord('a')]:
                continue
            while (stack and stack[-1] > ele and count[ord(stack[-1])-ord('a')] > 0):
                visited[ord(stack[-1])-ord('a')] = False
                stack.pop()
            stack.append(ele)
            visited[ord(ele)-ord('a')] = True
        return ''.join(stack)


s = Solution()
# assert s.removeDuplicateLetters('') == ''
# assert s.removeDuplicateLetters('ab') == 'ab'
# assert s.removeDuplicateLetters('aba') == 'ab'
# assert s.removeDuplicateLetters('bab') == 'ab'
assert s.removeDuplicateLetters('bcabc') == 'abc'
# assert s.removeDuplicateLetters('cbacdcbc') == 'acdb'
# assert s.removeDuplicateLetters('abca') == 'abc'
# assert s.removeDuplicateLetters('abcdabcd') == 'abcd'
# assert s.removeDuplicateLetters('cbacdcbc') == 'acdb'
