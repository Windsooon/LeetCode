class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        if not S:
            return 0
        self.cache = {}
        return self.dfs(0, len(S), S) % 1000000007

    def dfs(self, start, end, S):
        if (start, end) in self.cache:
            return self.cache[(start, end)]
        String = S[start:end]
        count = 0
        for char in 'abcd':
            try:
                start_index = String.index(char) + start
                end_index = String.rindex(char) + start
            except ValueError:
                continue
            count += self.dfs(start_index+1, end_index, S) + 2 if start_index != end_index else 1
        self.cache[(start, end)] = count
        return count

s = Solution()
S = 'ababa'
print(s.countPalindromicSubsequences(S))
