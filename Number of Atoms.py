class Solution:
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        num = ''
        stack = [['', 1]]
        type = []
        for f in fomula[::-1]:
            if f.isdigit():
                num += f
            elif f == ')':
                stack.append(['', int(num)])
                num = ''
            elif f == '(':
                stack[-1][0] += type[-1] * (int(num)-1)
            else:
                if f.isupper():
                    type.append(f)
                else:
                    type[-1] += f
                stack[-1][0] += f
