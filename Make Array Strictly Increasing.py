import bisect

class Solution:
    def makeArrayIncreasing(self, arr1, arr2):
        arr2.sort()
        self.cache = dict()
        ans = self.recursion(float('-inf'), 0, arr1, arr2)
        if ans == float('inf'):
            return -1
        else:
            return ans


    def recursion(self, pre, index, arr1, arr2):
        if (pre, index) in self.cache:
            return self.cache[(pre, index)]
        if index == len(arr1):
            return 0
        available_lst = self.find(pre, arr2)
        if not available_lst:
            if arr1[index] > pre:
                res = self.recursion(arr1[index], index+1, arr1, arr2)
                self.cache[(pre, index)] = res
                return res
            else:
                return float('inf')
        else:
            res = float('inf')
            for l in available_lst:
                res = min(res, 1 + self.recursion(l, index+1, arr1, arr2))
            if arr1[index] > pre:
                res = min(res, self.recursion(arr1[index], index+1, arr1, arr2))
            self.cache[(pre, index)] = res
            return res

    def find(self, pre, arr2):
        index = bisect.bisect_right(arr2, pre)
        if index == len(arr2):
            return []
        else:
            return arr2[index:]

class Solution:
    def makeArrayIncreasing(self, arr1, arr2):
        arr2.append(float('-inf'))
        arr2.sort()
        dp = [[float('inf')] * len(arr1) for i in range(len(arr2))]
        # dp[i][j] 
        for i in range(len(arr2)):
            if arr2[i] > arr1[-1]:
                if self.find(arr2[i], arr2):
                    dp[-1][i] = 1
                else:
                    dp[-1][i] = float('inf')
            else:
                dp[-1][i] = 0
        for i in range(len(arr1)-2, -1, -1):
            for j in range(len(arr2)):
                k = self.get_index(arr2[j], arr2)
                k2 = self.get_index(arr1[i], arr2)
                if arr2[j] > arr1[i]:
                    if k == len(arr2):
                        dp[i][j] = float('inf')
                    else:
                        dp[i][j] = 1 + dp[i+1][k]
                else:
                    if k2 == len(arr2):
                        breakpoint()
                        dp[i][j] =  1 + dp[i+1][k]
                    else:
                        dp[i][j] = min(1 + dp[i+1][k], dp[i+1][k2])
        print(dp)
        return dp[0][0]


    def find(self, pre, arr2):
        index = bisect.bisect_right(arr2, pre)
        if index == len(arr2):
            return False
        return True

    def get_index(self, pre, arr2):
        return bisect.bisect_right(arr2, pre)

arr1 = [1,5,3,6,7]
arr2 = [1,3,2,4]
s = Solution()
print(s.makeArrayIncreasing(arr1, arr2))
