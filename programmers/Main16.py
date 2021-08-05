def solution(s):
    answer = True
    stack = []
    check = ['(', ')']
    for i in range(len(s)):
        if stack == []:
            stack.append(s[i])
        else:
            if stack[-1] == check[0] and s[i] == check[1]:
                stack.pop()
            else:
                stack.append(s[i])
    if stack != []:
        answer = False
    return answer


print(solution("()()"))
