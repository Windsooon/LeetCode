class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        lst = str.split(' ')
        pattern_dic = dict()
        if len(pattern) != len(lst):
            return False
        for i in range(len(pattern)):
            if pattern[i] in pattern_dic:
                if pattern_dic.get(pattern[i], -1) != lst[i]:
                    return False
            else:
                if lst[i] in pattern_dic.values() :
                    return False
                pattern_dic[pattern[i]] = lst[i]
        return True

s = Solution()
pattern = "abba"
str = "dog cat cat dog"
assert s.wordPattern(pattern, str) is True
pattern = "abba"
str = "dog cat cat fish"
assert s.wordPattern(pattern, str) is False
pattern = "aaaa"
str = "dog cat cat dog"
assert s.wordPattern(pattern, str) is False
pattern = "abba"
str = "dog dog dog dog"
assert s.wordPattern(pattern, str) is False
