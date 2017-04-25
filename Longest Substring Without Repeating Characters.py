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
                diff = i - dic[s[i]]
                if diff > len(answer):
                    max_len = diff
                    answer = s[point:point+max_len]
                point = dic[s[i]] + 1
            else:
                answer = s[point:i+1]
            dic[s[i]] = i
        return answer or s

c = Solution()
print(c.lengthOfLongestSubstring('abczzbcd'))
