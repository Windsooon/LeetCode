class Solution:
    def findWords(self, words):
        ans = []
        keyboard_rows = [
            set(list('qwertyuiop')), set(list('asdfghjkl')),
            set(list('zxcvbnm'))]
        for w in words:
            for row in keyboard_rows:
                if not set(w.lower()) - row:
                    ans.append(w)
        return ans

s = Solution()
words = ["Hello", "Alaska", "Dad", "Peace"]
print(s.findWords(words))
