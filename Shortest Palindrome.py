class Solution:
    def shortestPalindrome(self, s):
        if not s:
            return ''
        for i in range(len(s), 0, -1):
            if self.isPalindrome(s[:i]):
                return s[::-1][:len(s)-i] + s

    def isPalindrome(self, s):
        left, right = 0, len(s)-1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

s = Solution()
print(s.shortestPalindrome('aacecaaa'))
print(s.shortestPalindrome('abcd'))
print(s.shortestPalindrome('abab'))
print(s.shortestPalindrome('aab'))
print(s.shortestPalindrome('baa'))
