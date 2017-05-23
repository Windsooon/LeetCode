class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        z = 0
        for k in range(0, len(s)-1): 
            if roman[s[k]] < roman[s[k+1]]:
                z -= roman[s[k]]
            else:
                z += roman[s[k]]
        return z + roman[s[-1]]

b = Solution()
print(b.romanToInt('IV'))
