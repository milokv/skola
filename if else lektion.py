from typing import List, Any

print("Car requirements")
a = int(input("What is your net worth in USD? "))
if  a > 100000:
    vip = True
else: vip = False
b = int(input("How old are you?  "))
c = input("Whats your name?   ")
if c == ("Milo"):
    banned = True
else: banned = False
if b >= 18 and vip and not banned:
    print("ACCEPTED")
elif b >= 18 and vip and banned:
    print("BANNED")
elif b < 18 and not vip and not banned:
    print("YOUNG AND BROKE")
elif b < 18:
    print("TOO YOUNG")
elif b >= 18 and not vip and not banned:
    print("JUST NOT RICH ENOUGH")

n1 = False
n2 = False
n3 = False
num1 = int(input("Write a number"))
num2 = int(input("Write a second number"))
num3 = int(input("Write a third number"))

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

maxnumber = max_num(num1, num2, num3)
print(f"the largest number is {maxnumber}!")


def max_num2(num1, num2, num3):
    return max(num1, num2, num3)

maxnumber2 = max_num2(num1, num2, num3)
print(f"largest number is: {maxnumber2}!!")

def maxnum3(num1, num2, num3):
    max_num3 = [num1, num2, num3]
    max_num3.sort()
    return max_num3[-1]

maxnumber3 = maxnum3(num1, num2, num3)
print("largest number is %s!" % maxnumber3)
#3 olika exempel, också lite bonus format för att printa variablar :)