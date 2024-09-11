def compare_number(num1, num2):
    if num1 > num2:
        return "num1 is bigger"
    elif num1 < num2:
        return "num2 is bigger"
    else:
        return "both are equal"


num1 = float(input("enter 1st value: "))
num2 = float(input("enter 2nd value: "))
result = compare_number(num1, num2)
print(result)
