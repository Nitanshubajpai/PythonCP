
n=int(input())
count=0
a=[]
while True:
    a.append(n%10)
    n=n//10
    if n==0:
        break
for y in range(len(a)):
    if a[y]==1 or a[y]==0 or a[y]==8:
        count=count+1
    else:
        pass
if count==len(a):
    print("YES")
else:
    print("NO")
