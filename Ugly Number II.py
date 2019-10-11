class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        current_two = current_three = current_five = 0
        u = [1]
        while n-1:
            next_v = min(u[current_two] * 2, u[current_three] * 3, u[current_five] * 5)
            u.append(next_v)
            if next_v == u[current_two] * 2:
                current_two += 1
            if next_v == u[current_three] * 3:
                current_three += 1
            if next_v == u[current_five] * 5:
                current_five += 1
            n -= 1
        print(u)
        return u[-1]

s = Solution()
print(s.nthUglyNumber(11))
