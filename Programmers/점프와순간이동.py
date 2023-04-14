def solution(n):
    ans = 0
    k=0
    tmp=1
    while True :
        if n==1:
            break
        if n%2 ==0 :
            n=n//2
        else:
            tmp+=1
            n-=1
    return tmp