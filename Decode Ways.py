class Solution:
    def numDecodings(self, s):
        # 226
        if not self.isvalid(s):
            return 0
        self.s = s
        self.cache = dict()
        return self.dfs(s, 0)

    def dfs(self, s, count):
        if s in self.cache:
            return self.cache[s]
        if not s:
            return 1
        if s[0] == '0':
            self.cache[s] = 0
            return 0
        if len(s) == 1:
            return 1
        first = self.dfs(s[1:], count)
        if int(s[0]) > 2:
            second = 0
        elif (int(s[0]) == 2 and int(s[1]) <= 6) or int(s[0]) == 1:
            second = self.dfs(s[2:], count)
        else:
            second = 0
        self.cache[s] = first + second
        return first + second

    def isvalid(self, s):
        if not s or s[0] == '0':
            return False
        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i-1] not in ('1', '2'):
                    return False
        return True

class Solution:
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0
        # [0] * 3
        # [0, 0, 0]
        dp = [0] * (len(s)+1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
        # [1, 1, 0]
        for i in range(2, len(dp)):
            count = 0
            if s[i-1] != '0':
                count += dp[i-1]
            if self.valid(int(s[i-2]), int(s[i-1])):
                count += dp[i-2]
            dp[i] = count
        return dp[-1]

    def valid(self, a, b):
        if a == 0:
            return False
        elif a == 1:
            return True
        elif a == 2:
            if b <= 6:
                return True
        return False

class Solution:
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0
        # 226
        pre_pre = pre = 1
        # '226'
        for i in range(2, len(s)+1):
            count = 0
            if s[i-1] != '0':
                # count = 1
                count += pre
            if self.valid(int(s[i-2]), int(s[i-1])):
                count += pre_pre
            pre_pre, pre = pre, count
        return pre

    def valid(self, a, b):
        if a == 0:
            return False
        elif a == 1:
            return True
        elif a == 2:
            if b <= 6:
                return True
        return False


s = Solution()
str = '17'
assert s.numDecodings(str) == 2
str = '10'
assert s.numDecodings(str) == 1
str = '306'
assert s.numDecodings(str) == 0
str = '12'
assert s.numDecodings(str) == 2
str = '226'
assert s.numDecodings(str) == 3
str = '0'
assert s.numDecodings(str) == 0
str = '27'
assert s.numDecodings(str) == 1
str = '101'
assert s.numDecodings(str) == 1
