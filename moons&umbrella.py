t = int(input())
for i in range(t):
    x, y = map(int, input().split(" "))
    S = input()
    price = 0
    pre = 'A'
    for j in range(len(S)):
        if S[j]=='J':
            if pre=='C':
                price = price + x
                print(price)
            pre = 'J'
        elif S[j]=='C':
            if pre=='J':
                price = price + y
                print(price)
            pre=='C'
            
    print("Case #{}: {}".format(i+1, price))
