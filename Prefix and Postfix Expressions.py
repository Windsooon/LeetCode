class Soulution:
    def prepost(self, string):
        oper, answer = [], []
        d = {
            "+": 1, "-": 1,
            "*": 2, "/": 2}
        for k, v in enumerate(string):
            if v in d.keys():
                if not oper:
                    oper.append(v)
                elif d[oper[-1]] > d[v]:
                    answer.append(oper.pop())
                    oper.append(v)
                else:
                    oper.append(v)
            else:
                answer.append(v)
        answer = answer + oper[::-1]
        return answer

a = Soulution()
print(a.prepost("A*B+C*D"))
