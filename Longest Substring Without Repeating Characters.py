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

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        self.longest = 1
        for i in range(len(s)):
            seen = set()
            if len(s) - i > self.longest:
                self.dfs(s, i, 0, seen)
        return self.longest


    def dfs(self, s, index, count, seen):
        if s[index] in seen:
            self.longest = max(self.longest, count)
            return
        else:
            count += 1
            self.longest = max(self.longest, count)
        tem = seen.copy()
        tem.add(s[index])
        if index+1 < len(s):
            self.dfs(s, index+1, count, tem)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        dp = [0] * len(s)
        dp[0] = 1
        dic = dict()
        dic[s[0]] = 0
        longest = 0
        for i in range(1, len(s)):
            if s[i] in dic:
                dp[i] = min(i-dic[s[i]], dp[i-1] + 1)
            else:
                dp[i] = dp[i-1] + 1
            dic[s[i]] = i
            if longest < dp[i]:
                longest = dp[i]
        return longest




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
