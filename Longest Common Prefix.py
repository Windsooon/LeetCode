class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = ''
        # * is the unpacking operator, essential here
        for z in zip(*strs):
            break
        return prefix

a = Solution()
c = ["aa", "a"]
a.longestCommonPrefix(c)
