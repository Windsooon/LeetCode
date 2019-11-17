class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        current = x
        lst = []
        while current:
            now = current % 10
            lst.append(now)
            current //= 10
        level = 1
        for i in range(len(lst)-1, -1, -1):
            lst[i] *= level
            level *= 10
        return sum(lst) == x
