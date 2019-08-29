class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        if flowerbed[0] == 0:
            init = 1/3
        else:
            init = 0
        for l in flowerbed:
            if l == 0:
                init += 1/3
                if init == 1:
                    n -= 1
                    init = 1/3
                    if n == 0:
                        return True
            else:
                init = 0
        return False

s = Solution()
flowerbed = [1,0,0,0,0,0,1]
n = 2
assert s.canPlaceFlowers(flowerbed, n) is True
flowerbed = [1,0,0,0,0,1]
n = 2
assert s.canPlaceFlowers(flowerbed, n) is False
flowerbed = [1,0,0,0,1]
n = 1
assert s.canPlaceFlowers(flowerbed, n) is True
