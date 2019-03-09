def minOperations(n):
    def helper(num):
        if num == '0':
            return '1'
        else:
            return '0'

    def recu(n, time, visited):
        if n == '0' * len(n):
            return time
        if n in visited:
            return
        visited.add(n)
        time += 1
        for i in range(len(n)-1, -1, -1):
            if n[i] == '1':
                tem = recu(n[:-1] + helper(n[-1]), time, visited)
                if tem:
                    return tem
                tem2 = recu(n[:i-1] + helper(n[i-1]) + n[i:], time, visited)
                if tem2:
                    return tem2

    bin_number = bin(n)[2:]
    time = 0
    visited = set()
    return recu(bin_number, time, visited)


print(minOperations(156))
