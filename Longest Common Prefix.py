class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        ans = strs[0]
        for k in range(1, len(strs)):
            d = ""
            for i in range(min(len(ans), len(strs[k]))):
                if ans[i] == strs[k][i]:
                    d += ans[i]
                else:
                    break
            ans = d
        return ans

a = Solution()
c = ["aa", "a"]
print(a.longestCommonPrefix(c))
