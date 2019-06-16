class Solution:
    def addOperators(self, num, target):
        if not num:
            return []
        self.res = []
        # breakpoint()
        self.dfs(num, '', 0, 0, target)
        return self.res

    def dfs(self, num, path, prev, val, target):
        # 1. cache
        # 2. stop case
        if not num:
            if val == target:
                self.res.append(path)
            return
        # 3. edge case

        # 4. for loop
        for i in range(1, len(num)+1):
            # 5. check valid
            # 6. update value
            if len(num[:i]) > 1 and num[0] == '0':
                break

            if not path:
                self.dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), target)
                continue
            # edge case
            # 7. recursion
            after = num[:i]
            self.dfs(num[i:], path+'+'+after, int(after), val+int(after), target)
            self.dfs(num[i:], path+'-'+after, -int(after), val-int(after), target)
            self.dfs(num[i:], path+'*'+after, prev*int(after), (val-prev)+prev*int(after), target)
                # 8. reset value
# 
# 
# class Solution(object):
#     def addOperators(self, num, target):
#         """
#         :type num: str
#         :type target: int
#         :rtype: List[str]
#         """
#         results = []
#         self.helper(num, 0, target, 0, 0, "", results)
#         return results
#     
#     def helper(self, string, start, target, sum_so_far, last, path, results):
#         if start == len(string) and sum_so_far == target:
#             results.append(path)
#         
#         for end in range(start+1, len(string)+1):
#             sub_string = string[start:end]
#             print(sub_string)
#             if len(sub_string) > 1 and sub_string[0] == '0':
#                 break
#             cur = int(sub_string)
#             if start == 0:
#                 self.helper(string, end, target, sum_so_far + cur, cur, path + sub_string, results)
#             else:
#                 self.helper(string, end, target, sum_so_far + cur, cur, path + "+" + sub_string, results)
#                 self.helper(string, end, target, sum_so_far - cur, -cur, path + "-" + sub_string, results)
#                 self.helper(string, end, target, sum_so_far - last + cur * last, cur * last, path + "*" + sub_string, results)




s = Solution()
# print(s.addOperators("123", 15))
print(s.addOperators("000", 0))
# print(s.addOperators("123", 6))
# print(s.addOperators("232", 8))
# print(s.addOperators("105", 5))
# print(s.addOperators("00", 0))
