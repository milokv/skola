num1 = 123
num2 = 2
num3 = 4
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
max_num(num1, num2, num3)
if num1 == True:
    print("NUMBER 1")
else: print("No")