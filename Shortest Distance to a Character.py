class Solution:
    def shortestToChar(self, S, C):
        # find the index of C
        lst = []
        for i in range(len(S)):
            if S[i] == C:
                lst.append(i)
        if len(lst) == 1:
            lst = lst*2
        dis_list = []
        for i in range(len(lst)-1):
            # [(3, 5), (5, 6)]
            dis_list.append((lst[i], lst[i+1]))
        ans = []
        k = 0
        for i in range(len(S)):
            if i > dis_list[k][1] and k < len(dis_list)-1:
                k += 1
            if S[i] == C:
                ans.append(0)
            else:
                ans.append(min(abs(dis_list[k][0]-i), abs(dis_list[k][1]-i)))
        return ans

S = "aaba"
C = 'b'
s = Solution()
print(s.shortestToChar(S, C))
