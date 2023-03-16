import sys
input = sys.stdin.readline
from collections import defaultdict

win = defaultdict(set)
lose = defaultdict(set)

n = int(input())
m = int(input())
for _ in range(m):
    a,b = map(int,input().split())
    win[b].add(a)
    lose[a].add(b)
for i in range(1,n+1):
    for w in win[i]:
        lose[w].update(lose[i])
    for l in lose[i]:
        win[l].update(win[i])
for i in range(n):
    print(n-1-len(win[i+1])-len(lose[i+1]))
