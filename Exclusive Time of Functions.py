class Solution:
    def exclusiveTime(self, N, logs):
        ans = [0] * N
        stack = []
        prev_time = 0
        for log in logs:
            fn, typ, time = log.split(':')
            fn, time = int(fn), int(time)
            if typ == 'start':
                if stack:
                    ans[stack[-1]] += time - prev_time 
                stack.append(fn)
                prev_time = time
            else:
                ans[stack.pop()] += time - prev_time + 1
                prev_time = time + 1
        return ans

s = Solution()
# print(s.exclusiveTime(1, ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]))

print(s.exclusiveTime(2, ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]))
