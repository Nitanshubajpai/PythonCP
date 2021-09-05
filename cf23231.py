t=int(input())

for i in range(t):
    k = int(input())
    p=[]
    x=(k//7)+1
    for j in range(x):
        p.append("Rohit")
    for j in range(x):
        p.append("Dhawan")
    for j in range(x):
        p.append("kohli")
    for j in range(x):
        p.append("Yuvraj")
    for j in range(x):
        p.append("Raina")
    for j in range(x):
        p.append("Dhoni")
    for j in range(x):
        p.append("Sir Jadeja")

    print(p[k-(7*(k//7))-1])
