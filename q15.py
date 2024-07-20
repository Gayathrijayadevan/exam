def factorial(a):
    fact=1
    for i in range(1,a+1):
        fact=fact*i

    return fact    

s=int(input("enter the number to find factorial:"))
a=factorial(s)
print("factorial=",a)