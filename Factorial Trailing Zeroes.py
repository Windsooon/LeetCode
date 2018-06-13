def cal(n):
    ans = 1
    while n >= 1:
        ans = ans * n
        n -= 1
    return ans

print(cal(20))
