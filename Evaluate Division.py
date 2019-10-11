import collections
import queue
class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        res = []
        parent = {}    # i.e. [a, b] then parent[a] = b
        weight = {}    # i.e. a / b = 2.0, then weight[a] = 2.0
        ufind = UnionFind(parent, weight)
        for i, edge in enumerate(equations):
            x1, x2 = edge[0], edge[1]
            val = values[i]
            if x1 not in parent and x2 not in parent:
                parent[x1] = x2
                parent[x2] = x2
                weight[x1] = val
                weight[x2] = 1
            elif x1 not in parent:
                parent[x1] = x2
                weight[x1] = val
            elif x2 not in parent:    # weight[x1] already exists, if make x2 be x1's parent. then weight[x1] will be overwrite.
                parent[x2] = x1
                weight[x2] = 1 / val
            else:
                ufind.union(x1, x2, val)
                
        breakpoint()
        for x1, x2 in queries:
            if x1 not in parent or x2 not in parent or ufind.find(x1) != ufind.find(x2):
                res.append(-1.0)
            else:
                factor1 = weight[x1]
                factor2 = weight[x2]
                res.append(factor1 / factor2)
        return res
        
class UnionFind():
    def __init__(self, parent, weight):
        self.parent = parent
        self.weight = weight

    def find(self, vertex):
        if self.parent[vertex] == vertex:
            return vertex
        root = self.find(self.parent[vertex])
        self.weight[vertex] *= self.weight[self.parent[vertex]]
        self.parent[vertex] = root
        return root

    def union(self, vertex1, vertex2, val):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)
        self.weight[root1]= self.weight[vertex2] * val / self.weight[vertex1]
        self.parent[root1] = root2


s = Solution()
# [["a","b"],["b","c"],["bc","cd"]]
# [1.5,2.5,5.0]
# [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# [["a","e"],["b","e"]]
# [4.0,3.0]
# [["a","b"],["e","e"],["x","x"]]

equations = [["a","e"],["b", "d"], ["a", "b"]]
values = [4.0,3.0,10]
queries = [["a","b"],["e","e"],["x","x"]]

print(s.calcEquation(equations, values, queries))
