from sys import exit
a=[]
for i in range(5):
    a.append(input())
for i in range(5):
   if a[i]== '42':
       exit(0)
   else:
      print (a[i])

