import random

def user_input():
    user_input=input("Enter your 6 digit lottery number, seperated by commas: ")
    user_numc=user_input.split(',')
    user_numi={int(number) for number in user_numc}
    return user_numi

def winning_number():
    win_number=set()
    while len(win_number)<6:
        win_number.add(random.randint(1, 20))
    return win_number
i='y'
while i=='y' or i=='Y':
    lottery_number = winning_number()
    user_number = user_input()
    result=user_number.intersection(lottery_number)
    print("You matched {}, You won ${}".format(result, 100*len(result)))
    print("The winning lottery number is {}".format(lottery_number))
    print("***************************")
    i=input("Enter y to continue: ")
