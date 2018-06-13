class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if len(needle) > len(haystack) or not haystack:
            return -1
        pointer = 0
        # for in a
        for i in range(len(haystack)):
            if haystack[i] == needle[pointer]:
                if pointer < len(needle) - 1:
                    pointer += 1
                else:
                    return i-len(needle)+1
            elif haystack[i] == needle[0]:
                pointer = 1
            else:
                pointer = 0
        return -1


a = "mississippi"
b = "issip"

s = Solution()
print(s.strStr(a, b))
# adcadcd dcd
# iiiip iiip
