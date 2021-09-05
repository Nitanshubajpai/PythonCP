t = int(input())
for i in range(t):
    n, k = map(int, input().split(" "))
    s = input()
    g = 0
    for j in range(n//2):
        if (s[j]!=s[n-j-1]):
            g=g+1
    if g==k:
        fin = 0
    elif k>g:
        fin = k - g
    else:
        fin = g - k
    print(f"Case #{i}: {fin}")
