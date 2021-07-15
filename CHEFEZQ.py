import math
T = int(input())
for i in range(T):

    n,k = map(int,input().split())
    Q = list(map(int,input().split()))
    f = 0
       
    for z in range(n-1):
        if Q[z] >= k:
            x = Q[z]-k
            Q[z+1] = Q[z+1] + x
            
        else:
            print(z+1)
            f = 1
            break
    if f == 0:
        if Q[-1]<k:
            print(n)
        else:
            print(n+Q[-1]//k)


