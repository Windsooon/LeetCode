import collections

class Solution:
    def minTransfers(self, transactions):
        dic = self.build_graph(transactions)
        self.cache = dict()
        res = []
        for k, v in dic.items():
            if v != 0:
                res.append(v)
        return self.dfs(res)

    def build_graph(self, transactions):
        dic = collections.defaultdict(int)
        for tran in transactions:
            dic[tran[0]] -= tran[2]
            dic[tran[1]] += tran[2]
        return dic

    def dfs(self, res):
        if tuple(res) in self.cache:
            return self.cache[tuple(res)]
        if not res:
            return 0
        if res[0] == 0:
            return self.dfs(res[1:])
        ans = float('inf')
        for i in range(len(res)):
            tem = res[:]
            if tem[i] + tem[0] == 0:
                tem[i] = tem[0] = 0
                return 1 + self.dfs(tem[1:])
            if tem[i] * tem[0] < 0:
                change = min(-tem[0], tem[i])
                tem[0] += change
                tem[i] -= change
                current = 1 + self.dfs(tem[:])
                ans = min(current, ans)
        self.cache[tuple(res)] = ans
        return ans


s = Solution()
# print(s.minTransfers([[1,8,1],[1,13,21],[2,8,10],[3,9,20],[4,10,61],[5,11,61],[6,12,59],[7,13,60]]))
print(s.minTransfers([[0,3,2],[1,4,3],[2,3,2],[2,4,2]]))
# print(s.minTransfers([[0,1,1],[1,2,1],[2,3,4],[3,4,5]]))
