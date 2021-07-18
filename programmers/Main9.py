def solution(n, arr1, arr2):
    answer = []
    # for a1, a2 in zip(arr1, arr2):
    #     a12 = str(bin(a1 | a2))[2: ] # or
    #     a12 = '0' * (n - len(a12)) + a12
    #     a12 = a12.replace('1', '#')
    #     a12 = a12.replace('0', ' ')
    #     answer.append(a12)
    for i in range(n):
        num = str(bin(arr1[i]|arr2[i]))[2: ] #비트연산자 or
        num = '0'*(n-len(num)) + num #앞단에 자릿수에 맞게 '0'을 추가
        num = num.replace('1','#')
        num = num.replace('0', ' ')
        answer.append(num)
    return answer