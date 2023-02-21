# UPPGIFT 2
def partition(ratings):

    def split(lst, bits):
        ret = ([], [])
        for i, item in enumerate(lst):
            ret[(bits >> i) & 1].append(item)
        return ret

    target = sum(ratings) // 2
    best_distance = target
    best_split = ([], [])
    for bits in range(0, 1 << len(ratings)):
        parts = split(ratings, bits)
        distance = abs(sum(parts[0]) - target)
        if best_distance > distance:
            best_distance = distance
            best_split = parts
    return best_split

ratings = []
styrka1 = int(input("ettor?"))
styrka2 = int(input("tvåor?"))
styrka3 = int(input("treor"))
styrk4 = int(input("fyror?"))
for i in range(styrka1):
    ratings.append(1)
for i in range(styrka2):
    ratings.append(2)
for i in range(styrka3):
    ratings.append(3)
for i in range(styrka1):
    ratings.append(4)
output1 = partition(ratings)
lista123 = str(output1[:1])
print(output1)
print(lista123)
ettor = lista123.count("1")
tvåor = lista123.count("2")
treor = lista123.count("3")
fyror = lista123.count("4")
list456 = ("")
list456 = list456 + str(ettor) + " "
list456 = list456 + str(tvåor) + " "
list456 = list456 + str(treor) + " "
list456 = list456 + str(fyror)
print(list456)