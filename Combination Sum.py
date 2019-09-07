class Solution:
    def combinationSum(self, candidates, target: int):
        if not candidates:
            return []
        candidates.sort(reverse=True)
        self.ans = []
        self.dfs(0, candidates, target, [])
        return self.ans

    def dfs(self, index, candidates, target, lst):
        if target == 0:
            self.ans.append(lst)
            return
        elif index == len(candidates):
            return
        nums = target // candidates[index]
        for i in range(nums, -1, -1):
            if index < len(candidates) and target-(i*candidates[index]) >= 0:
                self.dfs(index+1, candidates, target-(i*candidates[index]), [candidates[index]]*i + lst)

s = Solution()
candidates = [2,3,6,7]
target = 7

candidates = [2,3,5]
target = 8
print(s.combinationSum(candidates, target))
