class Solution:
    def permuteUnique(self, nums):
        breakpoint()
        for n in nums:
            new_ans = []
            for l in ans:
                for i in range(len(l)+1):
                    new_ans.append(l[:i]+[n]+l[i:])
                    if i<len(l) and l[i]==n: break              #handles duplication
            ans = new_ans
        return ans

s = Solution()
print(s.permuteUnique([1, 2, 2]))
