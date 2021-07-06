def solution(n, words):
    answer = []
    cnt=0
    stack=[]
    for i in range(len(words)):
        if stack==[]:
            stack.append(words[i])
            cnt+=1
        else:
            if stack[-1][-1] != words[i][0] or words[i] in stack:
                cnt+=1
                break
            else:
                if stack[-1][-1] == words[i][0]:
                    stack.append(words[i])
                    cnt+=1
    if stack==words:
        return [0,0]
    elif cnt%n==0:
        answer.append(n)
        answer.append(cnt//n)
    else:
        answer.append(cnt%n)
        answer.append((cnt//n)+1)

    return answer