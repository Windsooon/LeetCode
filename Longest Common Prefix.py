class Solution(object):
    # 1. find minimal
    # 2. stop when not valid
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest 

a = Solution()
c = ["aa", "a"]
a.longestCommonPrefix(c)
