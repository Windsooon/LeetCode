class Solution:
    def maxDistToClosest(self, seats):
        dis = (0, 0)
        pre = 0
        seats = [1] + seats + [1]
        for i in range(1, len(seats)):
            if seats[i] == 1:
                if i - pre > dis[1]-dis[0]:
                    # dis = [1, 5]
                    dis = (pre, i)
                # pre = 5
                pre = i
        breakpoint()
        if dis[0] == 0:
            return dis[1]-1
        elif dis[1] == len(seats)-1:
            return dis[1]-dis[0]-1
        return (dis[1]-dis[0]) // 2


s = Solution()
print(s.maxDistToClosest([0,1,1,1,0,0,1,0,0]))
