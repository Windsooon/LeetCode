class Solution:
    def reconstructQueue(self, people):
        for i in range(len(people)):
            if self.check([], people[i]):
                tem_array = people[:]
                del tem_array[i]
                ans = self.dfs(tem_array, [people[i]])
                if ans:
                    return ans

    def dfs(self, array, pre):
        if not array:
            return pre
        for i in range(len(array)):
            if self.check(pre, array[i]):
                tem_array = array[:]
                del tem_array[i]
                next = pre[:]
                next.append(array[i])
                ans = self.dfs(tem_array, next)
                if ans:
                    return ans

    def check(self, pre, element):
        count = 0
        for i in range(len(pre)):
            if pre[i][0] >= element[0]:
                count += 1
        return count == element[1]

s = Solution()
print(s.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))
