friends = ["jim", "karen", "kevin"]
for test in range(3):
    print(friends[test])
    if test == 2:
        print("3")


n1 = input("skriv")
for i in n1:
    print("(" + i + ")")

n2 = int(input("skriv ett nummer"))
for i in range(n2):
    print("|" + i * " " + "\\")
    if i == n2-1:
        print("|" + i * "_" + "_" + "\\")
n = 0
n3 = int(input("skriv igen nmr"))
for i in range(0, n3+1):
    n = n + i

print(n)