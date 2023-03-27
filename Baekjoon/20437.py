import sys
input = sys.stdin.readline
from collections import defaultdict
n = int(input())

for _ in range(n):
    max_ans = 0
    min_ans = 10000
    w = input()[:-1]
    k = int(input())
    dic = defaultdict(list)
    for i,s in enumerate(w) :
        if w.count(s) >=k:
            dic[s].append(i)
    if not dic :
        print(-1)
        continue
    for v in dic.values() :
        for i in range(len(v)):
            if i>=k-1:
                tmp = v[i]-v[i-k+1]+1
                if tmp > max_ans:
                    max_ans = tmp
                if tmp < min_ans:
                    min_ans = tmp
    print(min_ans,max_ans)
