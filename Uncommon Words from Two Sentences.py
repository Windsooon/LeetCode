import collections

class Solution:
    def uncommonFromSentences(self, A, B):
        ans = []
        lstA = A.split()
        lstB = B.split()
        if len(lstA) > len(lstB):
            # make lstA shortest list
            lstA, lstB = lstB, lstA
        dicA = collections.defaultdict(int)
        dicB = collections.defaultdict(int)
        for l in lstA:
            dicA[l] += 1
        for l in lstB:
            dicB[l] += 1
        for k, v in dicA.items():
            if v == 1:
                if k not in dicB:
                    ans.append(k)
        for k, v in dicB.items():
            if v == 1:
                if k not in dicA:
                    ans.append(k)
        return ans

s = Solution()
A = "apple apple"
B = "banana"
print(s.uncommonFromSentences(A, B))
