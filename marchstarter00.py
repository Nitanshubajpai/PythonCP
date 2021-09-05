t= int(input())
for i in range(t):
    n , m = map(int, input().split())
    s = set(input().split())
    if (len(s)<m):
        print("Yes")
    else:
        print("no")
