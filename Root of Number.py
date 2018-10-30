def root(x, n):
    # 9, 2
    # binary search
    # 1, 9
    left, right = 1, x
    while right - left > 0.001:
        mid = (left+right)/2
        if mid**n > x:
            right = mid
        elif mid**n < x:
            left = mid
        else:
            break
    return mid

print(root(3, 2))
