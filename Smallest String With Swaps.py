import collections

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs):
        dic = self.create_graph(pairs)
        self.graph = collections.defaultdict(list)
        self.dfs_wrapper(len(s), dic)
        ans = [''] * len(s)
        visited = set()
        for i in range(len(s)):
            if i in self.graph and i not in visited:
                index_lst = self.graph[i]
                element_lst = [s[j] for j in index_lst]
                index_lst.sort()
                element_lst.sort(reverse=True)
                for index in index_lst:
                    visited.add(index)
                    ans[index] = element_lst.pop()
        return ''.join(ans)



    def create_graph(self, pairs):
        dic = collections.defaultdict(list)
        for p in pairs:
            dic[p[0]].append(p[1])
            dic[p[1]].append(p[0])
        return dic

    def dfs_wrapper(self, n, dic):
        visited = set()
        for i in range(n):
            if i not in visited:
                lst = []
                res = self.dfs(i, visited, dic, lst)
                self.graph[i] = res

    def dfs(self, index, visited, dic, lst):
        visited.add(index)
        lst.append(index)
        for post in dic[index]:
            if post not in visited:
                self.dfs(post, visited, dic, lst)
        return lst


s = Solution()
print(s.smallestStringWithSwaps("dcab", [[0,3],[1,2]]))
