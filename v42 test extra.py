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