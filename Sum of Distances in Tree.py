import collections
import queue

# How many edges we have?
# What inside the edges? number or string or val
class Solution:
    def sumOfDistancesInTree(self, N, edges):
        tree = collections.defaultdict(set)
        self.res = [0] * N
        self.count = [1] * N
        self.N = N
        for i, j in edges:
            tree[i].add(j)
            tree[j].add(i)
        self.post_order(0, tree, set([0]))
        self.pre_order(0, tree, set([0]))

        return self.res

    def post_order(self, node, tree, visited):
        for n in tree[node]:
            if n not in visited:
                visited.add(n)
                self.post_order(n, tree, visited)
                self.count[node] += self.count[n]
                self.res[node] += self.res[n] + self.count[n]

    def pre_order(self, node, tree, visited):
        for n in tree[node]:
            if n not in visited:
                self.res[n] = self.res[node] - self.count[n] + self.N - self.count[n]
                visited.add(n)
                self.pre_order(n, tree, visited)


N = 6
edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
s = Solution()
s.sumOfDistancesInTree(N, edges)
