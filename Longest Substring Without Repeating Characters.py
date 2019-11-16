import collections

class Solution:
    # 1. two pointer
    # 2. update the dict af first
    # 3. check valid after update the dict
    # 4. update the left pointer
    def lengthOfLongestSubstring(self, s: str) -> int:
        up = down = ans = 0
        dic = collections.defaultdict(int)
        while up < len(s):
            dic[s[up]] += 1
            if dic[s[up]] <= 1:
                ans = max(ans, up-down+1)
            while dic[s[up]] > 1:
                dic[s[down]] -= 1
                down += 1
            up += 1
        return ans


c = Solution()
print(c.lengthOfLongestSubstring('abcabcbb'))
print(c.lengthOfLongestSubstring('aabbcca'))
print(c.lengthOfLongestSubstring('aa'))
print(c.lengthOfLongestSubstring('ab'))
print(c.lengthOfLongestSubstring('a'))
print(c.lengthOfLongestSubstring('aba'))
print(c.lengthOfLongestSubstring('aaba'))
print(c.lengthOfLongestSubstring('abcda'))
print(c.lengthOfLongestSubstring('abab'))
