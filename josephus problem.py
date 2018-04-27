class solution:
    def josephus(self, n, k):
        last = 0
        for i in range(1, n+1):
            print('pre {0}'.format(last))
            last = (last+k) % i
            print('last {0}'.format(last))
        return last

s = solution()
print(s.josephus(20, 3))
