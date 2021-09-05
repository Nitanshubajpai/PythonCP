t=int(input())
for i in range(t):
    n = int(input()) 
    a = list(map(int,input().strip().split()))[:n] 
    a.sort(reverse=True)
    print(2*(a[0]-a[n-1]))

