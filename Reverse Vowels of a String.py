class Solution:
    def reverseVowels(self, s):
        if not s:
            return ''
        lst = list(s)
        left, right = 0, len(lst)-1
        while left < right:
            if lst[left].lower() in 'aeiou' and lst[right].lower() in 'aeiou':
                lst[left], lst[right] = lst[right], lst[left]
                left += 1
                right -= 1
            while lst[left].lower() not in 'aeiou':
                left += 1
                if left >= len(lst):
                    break
            while lst[right].lower() not in 'aeiou':
                right -= 1
                if right < 0:
                    break
        return ''.join(lst)

s = Solution()
str = "hello"
assert s.reverseVowels(str) == 'holle'
str = "leetcode"
assert s.reverseVowels(str) == 'leotcede'
str = "aA"
assert s.reverseVowels(str) == 'Aa'
