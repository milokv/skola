def make_teams(que):
    que.sort()
    if len(que)%2: que.insert(0,0)
    t1,t2 = [],[]
    while que:
        val = (que.pop(), que.pop())
        if sum(t1)>sum(t2):
            t2.append(val[0])
            t1.append(val[1])
        else:
            t1.append(val[0])
            t2.append(val[1])
    return(t1)


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
output1 = make_teams(ratings)
print(output1)
stringoutput = ""
stringoutput = str(output1.count(1))
stringoutput += str(output1.count(2))
stringoutput += str(output1.count(3))
stringoutput += str(output1.count(4))
print(stringoutput)