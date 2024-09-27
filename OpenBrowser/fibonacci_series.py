#Fibonacci series
number=int(input("Enter the Fibonacci Number:\n"))
a=0
b=1
print(a)
print(b)
for i in range(2,number):
    c=a+b
    a=b
    b=c
    print(c)