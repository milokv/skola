list = ["noll", "ett","två","tre","fyra"]
list.remove("två")
list2 = ["fem","sex"]
list.extend(list2)
list.sort()
print(list)
print(list[-3],list[-2],list[-1])
list.insert(1,"ett")
print(list)