class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) > len(num2):
            num2 = '0'* (len(num1) - len(num2)) + num2
        elif len(num2) > len(num1):
            num1 = '0'* (len(num2) - len(num1)) + num1
        add_one, ans = self.recursion(num1, num2, 10**(len(num1)-1))
        if add_one:
            ans += 10**(len(num1))
        return ans

    def recursion(self, num1, num2, level):
        if not num1 or not num2:
            return ans
        if len(num1) == 1 and len(num2) == 1:
            current_sum = int(num1[0]) + int(num2[0])
            return current_sum // 10, current_sum % 10
        pre, pre_sum = self.recursion(num1[1:], num2[1:], level//10)
        current = pre + int(num1[0]) + int(num2[0])
        current_sum = (current % 10) * level + pre_sum
        return current // 10, current_sum
