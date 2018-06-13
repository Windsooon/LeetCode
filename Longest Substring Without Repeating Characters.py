class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)
        left = right = ans = 0
        position = {}
        while right <= len(s)-1:
            if s[right] not in position.keys():
                # a: 0
                position[s[right]] = right
            else:
                left = max(left, position[s[right]] + 1)
                position[s[right]] = right
            ans = max(ans, right-left+1)
            right += 1
        return ans


c = Solution()
print(c.lengthOfLongestSubstring('a'))
print(c.lengthOfLongestSubstring('aa'))
print(c.lengthOfLongestSubstring('ab'))
print(c.lengthOfLongestSubstring('aba'))
print(c.lengthOfLongestSubstring('aaba'))
print(c.lengthOfLongestSubstring('abcda'))
print(c.lengthOfLongestSubstring('aabbcca'))
print(c.lengthOfLongestSubstring('aabbcca'))
print(c.lengthOfLongestSubstring('abab'))
