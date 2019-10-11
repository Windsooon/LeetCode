class Solution:
    def maximumSum(self, arr):
        dp_forward = [arr[0]] + [0] * (len(arr)-1)
        dp_backword = [0] * (len(arr)-1) + [arr[-1]]
        res = arr[0]
        for i in range(1, len(arr)):
            if dp_forward[i-1] < 0:
                dp_forward[i] = arr[i]
            else:
                dp_forward[i] = dp_forward[i-1] + arr[i]
            res = max(res, dp_forward[i])

        for i in range(len(arr)-2, -1, -1):
            if dp_backword[i+1] < 0:
                dp_backword[i] = arr[i]
            else:
                dp_backword[i] = dp_backword[i+1] + arr[i]
            res = max(res, dp_backword[i])

        for i in range(1, len(arr)-1):
            if arr[i] < 0:
                res = max(res, dp_forward[i-1] + dp_backword[i+1])
        return res

s = Solution()
print(s.maximumSum([8,-1,6,-7,-4,5,-4,7,-6]))
# print(s.maximumSum([2,1,-2,-5,-2]))
# print(s.maximumSum([1,-2,0,3]))
# print(s.maximumSum([1,-2,-2,3]))
# print(s.maximumSum([-1,-1,-1,-1]))
