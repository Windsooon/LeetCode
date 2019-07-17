class Solution:
    def findComplement(self, num: int) -> int:
        binary = list(bin(num))
        for i in range(2, len(binary)):
            if binary[i] == '0':
                binary[i] = '1'
            else:
                binary[i] = '0'
        num = int(''.join(binary), 2)
        return num

s = Solution()
print(s.findComplement(5))
