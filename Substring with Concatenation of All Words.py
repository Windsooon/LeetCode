class Solution:
    def findSubstring(self, s, words):
        if not words or not s:
            return
        # create dict
        ans = []
        dic = {}
        all_length = sum(len(w) for w in words)
        length = len(words[0])
        for w in words:
            if w in dic:
                dic[w] += 1
            else:
                dic[w] = 1

        for i in range(len(s)):
            str = s[i:i+all_length]
            str_dic = {}
            for k in range(0, len(str), length):
                if str[k:k+length] in str_dic:
                    str_dic[str[k:k+length]] += 1
                else:
                    str_dic[str[k:k+length]] = 1
            if str_dic == dic:
                ans.append(i)
        return ans


s = Solution()
# print(s.findSubstring('', ["foo", "bar"]))
print(s.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))
# print(s.findSubstring('barfoothefoobarman', []))
# print(s.findSubstring('barfoothefoobarman', ["foo","bar"]))
# print(s.findSubstring('barfoobar', ["foo", "bar"]))
# print(s.findSubstring('wordgoodgoodgoodbestword', ["word", "good", "best", "word"]))
