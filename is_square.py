# 1, 4, 5
def is_square(n):
    left, right = 0, n
    while right-left>1:
        mid = (left+right)//2
        v = mid**2
        if v == n:
            return True
        elif v > n:
            right = mid
        else:
            left = mid
    return False

print(is_square(4))
print(is_square(5))
print(is_square(16))
print(is_square(18))
print(is_square(49))
