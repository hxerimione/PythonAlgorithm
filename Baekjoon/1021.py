from collections import deque
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
arr = list(map(int,input().split()))
q = [i for i in range(1,N+1)]
q = deque(q)
answer = 0
for a in arr :
    if q.index(a) <N/2:
        for _ in range(q.index(a)):
            tmp = q.popleft()
            q.append(tmp)
            answer+=1
    else:
        for _ in range(N-q.index(a)):
            tmp = q.pop()
            q.appendleft(tmp)
            answer+=1
    q.popleft()
    N-=1     
print(answer)