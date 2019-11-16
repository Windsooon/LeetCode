import collections

class Solution:
    def groupStrings(self, strings):
        dic = collections.defaultdict(list)
        for i in range(len(strings)):
            current = []
            start = strings[i][0]
            for char in strings[i]:
                next_char = ord(char)-ord(start)
                if next_char < 0:
                    next_char += 26
                current.append(str(next_char)+'#')
            current_str = ''.join(current)
            dic[current_str].append(strings[i])
        res = []
        for k, v in dic.items():
            res.append(v)
        return res


lst = ["abc","am"]
s = Solution()
print(s.groupStrings(lst))
