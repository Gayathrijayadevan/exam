# 13.
from calculator import *

while True:

    print("1.addition \n 2.substraction \n 3.multiplication \n 4. division \n 5.break")

    a=int(input("enter our choice"))

    b=int(input("enter a number:"))
    c=int(input("enter another number:"))
    
    if a == 1:
        s=add(b,c)
        print("result=",s)
    elif a == 2:
        s=sub(b,c) 
        print("result=",s)
    elif a== 3:
        s=mul(b,c)
        print("result=",s)
    elif a== 4:
        s=div(b,c)     
        print("result=",s)
    elif a==5:
        break    
              


