
"""UPPGIFT 1"""
n1 = input("skriv")
for i in n1:
    print("(" + i + ")")


"""UPPGIFT 2"""
n2 = int(input("skriv ett nummer"))
for i in range(n2):
    print("|" + i * " " + "\\")
    if i == n2-1:
        print("|" + i * "_" + "_" + "\\")

"""UPPGIFT3"""

n3 = int(input("kvadrat"))
n3 = n3 - 2
for index in range(n3+1):
    if index == 1:
        print("|" + "‾‾‾" * n3 + "|")
    if index << n3:
        print("|" + "   " * n3 + "|")
    if index >= n3:
        print("|"+ "___" * n3 + "|")
              
"""UPPGIFt 4"""

n = 0
n4 = int(input("skriv igen nmr"))
for i in range(0, n4+1):
    n = n + i

print(n)

"""uppgift 5"""
x = int(input("skriv ett tal"))
y = int(input("skriv ett till tal"))
def sum(a,b):
    c = 0
    if b >= a:
        for i in range(a+1,b):
            c = c + i
    if a >= b:
        for i in range(b+1,a):
            c = c + i
    return c

xyz = sum(x,y)
print(xyz)