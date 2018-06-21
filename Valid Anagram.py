class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        def helper(string):
            tem_dict = {}
            for s in string:
                if s in tem_dict:
                    tem_dict[s] += 1
                else:
                    tem_dict[s] = 1
            print(tem_dict)
            return tem_dict
        return helper(s) == helper(t)


fir = "aacc"
las = "ccac"
s = Solution()
print(s.isAnagram(fir, las))
