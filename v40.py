list1 = ["ett", "två", "tre", "fyra", "fem"]
print(list1[0:4])
list2 = list1.copy()
list2.reverse()
print(list2)
element1 = list2[0]
print(element1)
list1.insert(3, element1)
print(list1.count(element1))

uppgift2 = [1, 2, 3, 4, 5]
uppgift2.append("1")
print(uppgift2)
uppgift2.extend(list1)
print(uppgift2)
# append lägger till det värde man skriver in i slutet av listan, extend lägger in en annan lista i slutet
uppgift2.pop(1)
print(uppgift2)
uppgift2.remove('fem')
print(uppgift2)
# pop tar bort värden i listan med den positionen som man anger,
# remove tar bort det första värdet som är likadant som det man anger
print(len(uppgift2))


def length(list):
    antal = 0
    for i in list:
        antal += 1
    return antal


print(length(uppgift2))
