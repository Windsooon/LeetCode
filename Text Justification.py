class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res, cur, num = [], [], 0
        for w in words:
            if len(cur) + len(w) + num > maxWidth:
                for i in range(maxWidth-num):
                    cur[i % (len(cur)-1 or 1)] += ' '
                res.append(''.join(cur))
                cur, num = [], 0
            cur += [w]
            num += len(w)
        return res + [' '.join(cur).ljust(maxWidth)]


words = ["This", "is", "an", "example", "of", "text", "justification."]
s = Solution()
print(s.fullJustify(words, 16))
