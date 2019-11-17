class Solution:
    # handle s[0] smartly
    def myAtoi(self, str: str) -> int:
        s = str.strip()
        sign = 1
        if not s:
            return 0
        current = ''
        if s[0] not in '-+0123456789':
            return 0
        if s[0] in '+-':
            sign = -1 if s[0] == '-' else 1
        for i in range(len(s)):
            if i == 0 and s[i] in '+-':
                continue
            if s[i] in ' .+-abcdefghijklmnopqrstuvwxyz':
                break
            else:
                current += s[i]
        if not current:
            return 0
        return min(2**31-1, max(-2**31, sign * int(current)))
