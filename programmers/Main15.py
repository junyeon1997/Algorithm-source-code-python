def solution(price, money, count):
    answer = -1
    tmp = 0
    for i in range(count):
        tmp += price*(i+1)
    if tmp > money:
        answer = tmp-money
    else:
        answer = 0
    return answer


print(solution(3, 20, 4))
