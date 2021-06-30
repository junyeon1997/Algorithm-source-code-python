n=int(input())
m=int(input())
result=[]
for i in range(round(m**(1/2)+1)):
    k=i*i
    if k in range(n,m+1):
        result.append(k)
if result==[]:
    print(-1)
else:
    print(sum(result))
    print(min(result))
   

