from collections import deque
import sys
input = sys.stdin.readline


def bfs(matrix, checklst, start):
    q = deque()
    cnt = 0
    checklst[start] = 1
    q.append(start)
    while q:
        k = q.popleft()
        for i in matrix[k]:
            if checklst[i] == 0:
                checklst[i] = 1
                cnt += 1
                q.append(i)
    return cnt


TC = int(input())
for _ in range(TC):
    N, M = map(int, input().split())
    matrix = [[] for _ in range(N+1)]
    checklst = [0 for i in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        matrix[a].append(b)
        matrix[b].append(a)
    print(bfs(matrix, checklst, 1))
