class Solution:
    def findRedundantConnection(self, edges):
        self.can = []
        self.dic = {}
        for e in edges:
            if e[0] not in self.dic:
                self.dic[e[0]] = e[0]
            if e[1] not in self.dic:
                self.dic[e[1]] = e[1]
            if self.find(e[0]) == self.find(e[1]):
                self.can.append(e)
            else:
                self.union(e[0], e[1])
        return self.can[-1]


    def find(self, index):
        return self.dic[index]

    def union(self, i, j):
        target = self.find(i)
        parent = self.find(j)
        for k, v in self.dic.items():
            if v == parent:
                self.dic[k] = target

s = Solution()
print(s.findRedundantConnection([[1,2], [1,3], [2,3]]))
print(s.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]))
print(s.findRedundantConnection([[1,4],[3,4],[1,3],[1,2],[4,5]]))
print(s.findRedundantConnection([[1,5],[3,4],[3,5],[4,5],[2,4]]))
