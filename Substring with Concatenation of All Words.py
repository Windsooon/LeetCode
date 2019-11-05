import collections

class Solution:
    def findSubstring(self, s: str, words):
        if not s or not words:
            return []
        word_len = len(words[0])
        total_len = sum(len(w) for w in words)
        dic = collections.defaultdict(int)
        ans = []
        for w in words:
            dic[w] += 1
        for i in range(len(s)):
            if self.check(i, s, dic.copy(), total_len, word_len):
                ans.append(i)
        return ans
    
    def check(self, index, s, dic, total_len, word_len):
        target = s[index:index+total_len]
        for i in range(0, len(target), word_len):
            current_word = target[i:i+word_len]
            if current_word not in dic:
                return False
            else:
                if dic[current_word] == 1:
                    del dic[current_word]
                else:
                    dic[current_word] -= 1
        return dic == {}
            


s = Solution()
print(s.findSubstring('barfoothefoobarman', ["foo","bar"]))
print(s.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))
print(s.findSubstring('wordgoodgoodgoodbestword', ["word", "good", "best", "word"]))
# print(s.findSubstring('', ["foo", "bar"]))
# print(s.findSubstring('barfoothefoobarman', []))
# print(s.findSubstring('barfoobar', ["foo", "bar"]))
