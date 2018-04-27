class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not haystack and not needle or not needle:
            return 0
        if not haystack:
            return -1
        for k, v in enumerate(haystack):
            if v == needle[0]:
                if haystack[k:k+len(needle)] == needle:
                    return k
        return -1


s = Solution()
print(s.strStr('hellk', 'lk'))
