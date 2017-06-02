class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        point = 0
        answer = ''
        dic = {}

        for i in range(len(s)):
            if s[i] in dic.keys():
                pass
            else:
                answer = s[point:i]
        return answer or s

c = Solution()
print(c.lengthOfLongestSubstring('abczzbcd'))
