friends = ["kevin","karen","jim"]
"""index 0       1        2"""
print(friends[1],friends[-1])
print(friends[0:],friends[1:])
lucky_numbers = [1,2,3,4,5]
friends.extend(lucky_numbers)
print(friends)
friends.append(123)
friends.insert(1,"kelly")
print(friends)
friends.pop()
print(friends.index("kevin"))
print(friends.index("kelly"))
friends.append("kelly")
print(friends.index("kelly"))
print(friends.count("kelly"))
friends.sort
print(friends)
friends2 = friends.copy()
