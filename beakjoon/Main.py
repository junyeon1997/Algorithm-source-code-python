K=int(input())
array=[]
for _ in range(K):
    num = int(input())
    if num==0:
        array.pop(-1)
    else:
        array.append(num)
print(sum(array))