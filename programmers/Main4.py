from collections import deque
def solution(people, limit):
    people.sort()
    q = deque(people)
    answer=0
    while q:
        if len(q)>=2:
            if q[0] + q[-1]>limit: #효율성 테스트 통과를 위해 최댓값과 최소값을 짝지어 비교했다.
                q.pop()
                answer+=1
            elif q[0] + q[-1] <=limit:
                q.popleft()
                q.pop()
                answer+=1
        else:
            if q[0]<=limit:
                q.pop()
                answer+=1
    return answer