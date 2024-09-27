year = int(input("Enter Year:\n"))

if year%4==0 and year%400==0:
   print("Leap Year")
elif year%100!=0:
    print("Not Leap Year")


