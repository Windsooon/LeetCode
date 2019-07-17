class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return ''
        lst = s.split(' ')
        for i in range(len(lst)):
            lst[i] = lst[i][::-1]
        return ' '.join(lst)

s = Solution()
print(s.reverseWords("Let's take LeetCode contest"))
