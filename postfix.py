class Solution:
    def solution(self, cal):
        answer = []
        oper = []
        for k, v in enumerate(cal):
            if v in 'abcdefghijklmnopqrstuvwxyz1234567890':
                answer.append(v)
            elif v == "*" or v == "/":
                if not oper or pri[oper.pop()] == 1:
                    oper.append(v)

            

A * B + C * D

AB * CD *+

