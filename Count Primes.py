class Solution:
    # def countPrimes(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     if n < 3:
    #         return 0

    #     if n % 2 == 0:
    #         matrix = [0, 1] * (n // 2)
    #     else:
    #         matrix = [0, 1] * (n // 2) + [1]
    #     matrix[0], matrix[1], matrix[2] = 0, 0, 1
    #     for i in range(2, n):
    #         if matrix[i]:
    #             current = 2
    #             while current*i < n:
    #                 matrix[current*i] = 0
    #                 current += 1
    #     return sum(matrix)

    def countPrimes(self, n):
        if n <= 2:
            return 0
        # if n % 2 == 0:
        #     res = [False, True] * (n // 2)
        # else:
        #     res = [False, True] * (n // 2) + [True]
        # res[2] = True
        res = [True] * n
        res[0] = res[1] = False
        for i in range(2, n):
            if res[i] is True:
                for j in range(2, (n-1)//i+1):
                    res[i*j] = False
        return sum(res)



s = Solution()
# 78497
# print(s.countPrimes(100))
print(s.countPrimes(999983))
# print(s.countPrimes(10))
# print(s.countPrimes(10))
# assert s.countPrimes(999983) == 2
