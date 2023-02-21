input1 = input("hej   ")
print(len(input1))
print(input1[0:3])
print(input1.index("a"))
print(str.islower(input1))

uppgift2 = input("Skriv längre mening   ")
print(len(uppgift2))
print(uppgift2.rfind("a"))
if uppgift2[-1] == '.':
   print("Last character is a period")
else: print("Last character is not a period")
print(uppgift2.endswith("."))
""" ^ 2 olika exempel"""
uppgift2 = uppgift2.lower()
uppgift2 = uppgift2.title()
uppgift2 = uppgift2.swapcase()
"""osäker om det skulle börja med små bokstäver eller stora bokstäver. man kan ta bort swapcase för att ändra det."""
print(uppgift2)

print(uppgift2.count(" ")+1)


result = len(uppgift2.split())

print("There are " + str(result) + " words.")

i = 1
while i < 4:
   i = (i+1)
   print("hej")
