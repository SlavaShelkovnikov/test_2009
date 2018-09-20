a = int(input())
b = int(input())
c = int(input())
if a > b and a > c:
    (a, c) = (c, a)
    if a > b:
        (a, b) = (b, a)
elif a > b and a <= c:
    (a, b) = (b, a)
elif a <= b and a > c:
    (a, c) = (c, a)
    (b, c) = (c, b)
if a <= b and a <= c and b > c:
    (b, c) = (c, b)
print(a, b, c)
