def sayhi(name1):
    print(f"Hello, {name1}!")
name = input("What is your name?\n")
sayhi(name)

num = input("cube")

def cube(num1):
    return num1*num1*num1
print(cube(int(num)))

#uppgiften här:

a = input("tal 1\n")
b = input("tal 2\n")
c = input("tal 3\n")

def minnum(a, b, c):
    return min(a, b, c)

print(minnum(a, b, c))
