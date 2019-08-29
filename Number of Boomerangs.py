import collections
class Solution:
    def numberOfBoomerangs(self, points):
        res = 0
        for i in range(len(points)):
            dic = collections.defaultdict(int)
            for j in range(len(points)):
                if i == j:
                    continue
                dic[self.get_distance(points[i], points[j])] += 1
            for k, v in dic.items():
                res += v*(v-1)
        return res
    def get_distance(self, A, B):
        return (A[0]-B[0])**2 + (A[1]-B[1])**2

s = Solution()
print(s.numberOfBoomerangs([[0,0],[1,0],[2,0]]))
