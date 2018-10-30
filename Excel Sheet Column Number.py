class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 'A' -> 1
        # 'AB' -> 28
        # 'ZY' -> 701
        # 'ZZ' -> 702
        # 'AZZ' -> 
        all_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        level = 0
        value = 0
        for k in s[::-1]:
            value += 26**level * (all_str.index(k)+1)
            level += 1
        return value

s = Solution()
print(s.titleToNumber('A'))
print(s.titleToNumber('AB'))
print(s.titleToNumber('ZY'))
print(s.titleToNumber('ZZ'))
