import random
i=input("Enter y to roll: ")
while i=='y' or i=='Y':
    n=random.randint(1,6)
    print("***************\n")
    print(" ___ ")
    print("|   |")
    print("|_{}_|".format(n))
    print("\n***************")
    i=input("Enter y to roll: ")
