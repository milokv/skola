a = float(input('1\n'))
b = float(input('2\n'))
c = float(input('3\n'))
d = float(input("4\n"))

if a == max(a, b, c, d): a = min(a, b, c, d)
elif b == max(a, b, c, d): b = min(a, b, c, d)
elif c == max(a, b, c, d): c = min(a, b, c, d)
elif d == max(a, b, c, d): d = min(a, b, c, d)
if a == max(a, b, c, d): print(f'the second largest number is {a}')
if b == max(a, b, c, d): print(f'the second largest number is {b}')
if c == max(a, b, c, d): print(f'the second largest number is {c}')
if d == max(a, b, c, d): print(f'the second largest number is {d}')
