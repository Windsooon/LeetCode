import collections

class Solution:
    def commonChars(self, A):
        if not A:
            return []
        res = []
        first_collection = [0] * 26
        for char in A[0]:
            first_collection[ord(char)-ord('a')] += 1
        for i in range(1, len(A)):
            second_collection = [0] * 26
            for char in A[i]:
                second_collection[ord(char)-ord('a')] += 1
            # compare
            for i in range(26):
                first_collection[i] = min(second_collection[i], first_collection[i])
        # get list
        for i in range(len(first_collection)):
            if first_collection[i]:
                res.extend([chr(ord('a')+i)]*first_collection[i])
        return res

s = Solution()
print(s.commonChars(["cool","lock","cook"]))
