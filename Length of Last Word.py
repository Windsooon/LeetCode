class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        count, start, last = 0, False, len(s)-1
        while last >= 0:
            if s[last] == ' ':
                if start:
                    return count
                else:
                    last -= 1
            else:
                start = True
                count += 1
                last -= 1
        return count


st = 'hello'
# st = 'hello world'
st = '  '
st = 'a '
s = Solution()
print(s.lengthOfLastWord(st))
