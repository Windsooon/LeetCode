class Solution:
    def numDecodings1(self, S):
        MOD = 10**9 + 7
        e0, e1, e2 = 1, 0, 0
        for c in S:
            if c == '*':
                f0 = 9*e0 + 9*e1 + 6*e2
                f1 = e0
                f2 = e0
            else:
                f0 = (c > '0') * e0 + e1 + (c <= '6') * e2
                f1 = (c == '1') * e0
                f2 = (c == '2') * e0
            e0, e1, e2 = f0 % MOD, f1, f2
        return e0

    def numDecodings(self, S):
        # set default value is 1
        answer = 1
        prev_answer = 1
        # the prev value is 1, 2 or not
        one, two = False, False
        for i in S:
            if i == '*':
                new = answer*9
                if one:
                    new += 9*prev_answer
                if two:
                    new += 6*prev_answer
                one, two = True, True
            else:
                # drop it if meet 0
                new = answer if (i > '0') else 0
                if one:
                    new += prev_answer
                if (two and i <= '6'):
                    new += prev_answer
                one = (i == '1')
                two = (i == '2')
            prev_answer = answer
            answer = new % (10**9 + 7)
        return answer

b = Solution()
print(b.numDecodings('**'))
print(b.numDecodings('1*'))
print(b.numDecodings('*1'))

print(b.numDecodings('*1*1*'))
