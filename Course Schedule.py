class Solution:
    def canFinish(self, numCourses: int, prerequisites):
        self.new = [True] * numCourses
        self.graph = self.create_graph(prerequisites)
        self.active = [False] * numCourses
        for i in range(len(self.new)):
            if self.new[i]:
                # found cycle
                if self.detect(i):
                    return False
        return True
                
    def detect(self, index):
        self.active[index] = True
        self.new[index] = False
        if index not in self.graph:
            self.active[index] = False
            return False
        for child in self.graph[index]:
            if self.active[child]:
                return True
            else:
                if self.detect(child):
                    return True
        self.active[index] = False
        return False
    
    def create_graph(self, prerequisites):
        import collections
        d = collections.defaultdict(list)
        for pre in prerequisites:
            d[pre[0]].append(pre[1])
        return d

s = Solution()
print(s.canFinish(2, [[1,0]]))
print(s.canFinish(2, [[1,0],[0,1]]))
print(s.canFinish(3,[[1,0],[1,2],[0,1]]))
