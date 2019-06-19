class Solution:
    def crackSafe(self, n, k):
        strings = ''.join(list(str(i) for i in range(k)))
        ans = '0'*n
        visited = set(['0'*n])
        length = k**n
        return self.dfs(ans, n, strings, visited, length)

    def dfs(self, ans, n, strings, visited, length):
        if len(visited) == length:
            return ans
        for s in strings:
            tem = ans[-n+1:]+s
            if tem not in visited:
                visited.add(tem)
                res = self.dfs(ans+s, n, strings, visited, length)
                if res:
                    return res
                visited.remove(tem)

s = Solution()
print(s.crackSafe(2, 2))
