bal=float(input())
wth=int(input())
if wth%5==0 and wth+0.50<=bal:
    bal=bal-wth-0.50
    print('%.2f'%bal)
else:
    print('Wrong input')        
