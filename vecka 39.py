import math
nr1 = int(input('First number:\n'))
nr2 = int(input("Second number\n"))
print("input: \n", nr1, "and", nr2, "\n", "output:", "\n", nr1 / nr2, "and", nr1 % nr2)


x = int(input('input an integer\n'))
y = float(input('input a float\n'))
x = float(x)
y = int(y)
print(x, y)
#floaten avrundas ner
#ceil avrundar upp
#floor avrundar ner
y = math.ceil(y)
x = math.floor(x)
print(y, x)
x = int(x)
print(math.gcd(x, y))
print((10 * 2) * 3.14159265358979323846264338327950288419716939937510)

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
