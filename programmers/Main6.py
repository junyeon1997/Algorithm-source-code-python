from collections import deque
#deque으로 풀이
def solution(prices):
    answer=[]
    q=deque(prices)
    while q:
        price=q.popleft()
        time=0
        for p in q:
            time+=1
            if price > p:
                break
        answer.append(time)
    return answer

#이중 반복문 풀이
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)-1):
        for j in range(i, len(prices)-1):
            if prices[i] > prices[j]:
                break
            else:
                answer[i]+=1
    return answer