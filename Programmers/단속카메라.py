def solution(routes):
    answer = 1
    routes = sorted(routes,key = lambda x: x[1])
    t = routes[0][1]
    for i in range(1,len(routes)):
        if t>=routes[i][0]:
            continue
        else:
            answer+=1
            t = routes[i][1]
    return answer