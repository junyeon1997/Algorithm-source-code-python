from collections import deque

def bfs(node, visited, graph):
    q=deque()
    q.append(node)
    visited[node]=1
    while q:
        now = q.popleft()
        for i in graph[now]:
            if visited[i]==0:
                q.append(i)
                visited[i] = visited[now]+1

def solution(n, edge):
    answer = 0
    visited = [0]*(n+1)
    graph = [[] for _ in range(n+1)]   
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)

    bfs(1, visited, graph)
    for m in visited:
        if m == max(visited):
            answer+=1
    return answer