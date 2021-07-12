def solution(n):
    answer = []
    tri=[[0 for i in range(0, j)] for j in range(1, n+1)]
    x=-1
    y=0
    num=1
    for a in range(0, n):
        for b in range(a, n):
            if a%3==0:
                x+=1
            elif a%3==1:
                y+=1
            else:
                x-=1
                y-=1
            tri[x][y]=num
            num+=1
    answer = sum(tri, [])
    return answer