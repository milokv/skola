import time
x = input("hej")
def recurse(x):
    if x <= 1:
        return x
    else:
        return((recurse(x-1) + recurse(x-2)))
print(recurse(int(x)))





y = int(input("triangle"))

def triangle(n):
    if n < 1:
        print("Error, number is too small")
    else:
        for i in range(1, n):
            print(" " * (n - i), "/", end="")
            print(" " * (2 * (i - 1) - 0), "\\", sep="")
        print(" " + "/" + "_" * ((2 * n) - 2) + "\\")

triangle(int(y))

jm