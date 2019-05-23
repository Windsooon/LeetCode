import collections

class Solution:
    def maxPoints(self, points):
        if len(points) <= 2: return len(points)
        d = collections.defaultdict(int) # (x,y) : count
        result = 0
        for i in range(len(points)):
            d.clear()
            overlap = 0
            curmax = 0
            for j in range(i+1, len(points)):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                if dx == 0 and dy == 0:
                    overlap += 1
                    continue
                gcd = self.getGcd(dx, dy)
                dx //= gcd
                dy //= gcd
                d[(dx,dy)] += 1
                curmax = max(curmax, d[(dx,dy)])
            result = max(result, curmax+overlap+1)
        return result

    def getGcd(self, a, b):
        if b == 0: return a
        return self.getGcd(b, a%b)


points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
s = Solution()
print(s.maxPoints(points))
