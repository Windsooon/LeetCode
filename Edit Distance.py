class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word1 = ' ' + word1
        word2 = ' ' + word2
        # ' horse'
        # [0, 1, 2, 3, 4, 5]
        lst = list(range(len(word1)))
        old = lst[:]
        for i in range(1, len(word2)):
            for j in range(len(word1)):
                if j == 0:
                    lst[j] += 1
                else:
                    if word2[i] == word1[j]:
                        lst[j] = old[j-1]
                    else:
                        lst[j] = min(lst[j-1], lst[j], old[j-1]) + 1
            old = lst[:]
        return lst[-1]


s = Solution()
print(s.minDistance('intention', 'execution'))
