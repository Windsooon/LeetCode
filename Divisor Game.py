class Solution:
    def divisorGame(self, N: int) -> bool:
        self.dic = {}
        return self.recursion(N)

    def recursion(self, N):
        if N in self.dic:
            return self.dic[N]
        if N == 1:
            return False
        elif N == 2:
            return True
        elif N == 3:
            return False
        # 1, 2, 3
        for i in range(1, N//2+1):
            # 1, 2, 
            if N % i == 0:
                if not self.recursion(N-1):
                    self.dic[N] = True
                    return True
        self.dic[N] = False
        return False

s = Solution()
print(s.divisorGame(5))
print(s.divisorGame(100))
