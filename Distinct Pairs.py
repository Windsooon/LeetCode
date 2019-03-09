# Complete the numberOfPairs function below.
def numberOfPairs(a, k):
    dic = dict()
    answer = set()
    for i in range(len(a)):
        if k - a[i] in dic:
            answer.add(a[i])
            answer.add(k - a[i])
        else:
            dic[a[i]] = i
    sum = 0
    print(answer)
    for an in answer:
        sum += a.count(an)
    return sum

print(numberOfPairs([6,6,3,9,3,5,1], 9))
