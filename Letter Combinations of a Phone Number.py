class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        if '' == digits:
            return []
        kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        results = [""]
        for i in range(len(digits)):
            tmp = []
            for l in results:
                for k in kvmaps[digits[i]]:
                    tmp.append(l+k)
            results = tmp
        return results
