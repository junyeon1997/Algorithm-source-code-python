def solution(s,array, answer):
    if s[0]=="push":
        array.append(int(s[1]))
    elif s[0]=="top":
        if array==[]:
            answer.append(-1)
        else:
            answer.append(array[-1])
    elif s[0]=="size":
        answer.append(len(array)) 
    elif s[0]=="empty":
        if array==[]:
            answer.append(1)
        else:
            answer.append(0)
    elif s[0]=="pop":
        if array==[]:
            answer.append(-1)
        else:
            p=array.pop(-1)
            answer.append(p)
    return answer

N=int(input())
stack=[]
answer=[]
for _ in range(N):
    s=input().split()
    result=solution(s, stack, answer)    
for i in range(len(result)):
    print(result[i])