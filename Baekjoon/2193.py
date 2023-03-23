import sys
input = sys.stdin.readline

n= int(input())
zero,one=0,1
for _ in range(n-1):
    tmp=zero
    zero = one + zero
    one = tmp
print(zero+one)