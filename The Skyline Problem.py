class Solution:
    def getSkyline(self, blds):
        """
        :type blds: List[List[int]]
        :rtype: List[List[int]]
        """
        if not blds: return []
        if len(blds) == 1: return [[blds[0][0], blds[0][2]], [blds[0][1], 0]]
        mid = len(blds) // 2
        left = self.getSkyline(blds[:mid])
        right = self.getSkyline(blds[mid:])
        return self.merge(left, right)
    
    def merge(self, left, right):
        h1, h2, res = 0, 0, []
        while left and right:
            if left[0][0] < right[0][0]:
                pos, h1 = left[0]
                left = left[1:]
            elif left[0][0] > right[0][0]:
                pos, h2 = right[0]
                right = right[1:]
            else:
                pos, h1 = left[0]
                h2 = right[0][1]
                left = left[1:]
                right = right[1:]
            H = max(h1, h2)
            if not res or H != res[-1][1]:
                res.append([pos, H])
        if left:
            res += left
        if right:
            res += right
        return res


s = Solution()
input = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
breakpoint()
print(s.getSkyline(input))
