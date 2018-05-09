class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # ' ', '', 'a', 'aba', 'ab a'
        # 'accb'
        left, right = 0, len(s)-1
        while left < right:
            if ord(s[left]) < 48 or ord(s[left]) > 122:
                left += 1
                continue
            if ord(s[right]) < 48 or ord(s[right]) > 122:
                right -= 1
                continue
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True


test_str = "0P"
test_str = "A man, a plan, a canal: Panama"
s = Solution()
print(s.isPalindrome(test_str))
