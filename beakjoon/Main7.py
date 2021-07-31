N = int(input())
cnt = 0
answer = 0
while answer <= N:
    cnt += 1
    answer += cnt
print(cnt-1)
