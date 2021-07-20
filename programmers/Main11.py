def solution(arr):
    answer = [0,0]
    n=len(arr)
    def div(x,y,n):
        check=arr[x][y] #네모칸을 확인해서 check과 같아야 통과
        for i in range(x, x+n):
            for j in range(y, y+n):
                if check!=arr[i][j]: #다르면 쪼갠다
                    div(x,y,n//2)
                    div(x,y+n//2,n//2)
                    div(x+n//2,y,n//2)
                    div(x+n//2,y+n//2,n//2)
                    return #같을 때까지 계속 쪼갠다
        answer[check]+=1 #압축과정을 통과해야 [0] or [1]에 +=1
        
    div(0,0,n)
    return answer

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))