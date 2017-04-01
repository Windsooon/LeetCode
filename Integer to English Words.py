class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven ' \
               'Twelve Thirteen Fourteen Fifteen Sixteen Seventeen ' \
               'Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()

        def recursive(num):
            if num < 20:
                return to19[num-1:num]
            elif num < 100:
                return [tens[num//10-2]] + recursive(num % 10)
            elif num < 1000:
                return [to19[num//100-1]] + ['Hundred'] + \
                    recursive(num % 100)
            else:
                for k, v in enumerate(('Thousand', 'Million', 'Billion'), 1):
                    if num < 1000**(k+1):
                        return recursive(num//1000**k) + \
                            [v] + recursive(num % 1000**k)
        return ' '.join(recursive(num)) or 'Zero'
