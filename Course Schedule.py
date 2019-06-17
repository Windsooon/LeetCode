class Solution:
    def canFinish(self, numCourses, prerequisites):
        self.dic = {}
        self.visited = {}
        # need to take this course first
        # [[1, 0]], 0 is needed
        needed = set()
        # [[1, 0]], 1 is needed
        taked = set()
        for p in prerequisites:
            taked.add(p[0])
            needed.add(p[1])
        finish_course = needed-taked
        for f in finish_course:
            self.dic[f] = True
        for p in prerequisites:
            if not self.dp(p[0], prerequisites):
                return False
        return True

    def dp(self, num, prerequisites):
        if num in self.dic:
            return self.dic[num]
        lst = []
        for i in range(len(prerequisites)):
            if i not in self.visited:
                if prerequisites[i][0] == num:
                    self.visited[i] = True
                    lst.append(prerequisites[i][1])
        if not lst:
            return False
        for l in lst:
            if not self.dp(l, prerequisites):
                self.dic[num] = False
                return False
        self.dic[num] = True
        return True

s = Solution()
print(s.canFinish(2, [[1,0]]))
print(s.canFinish(2, [[1,0],[0,1]]))
