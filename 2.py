A = int(input())
B = int(input())
counter = 0
while A > 0 or B > 0:
    if A % 2 != B % 2:
        counter += 1
    A = A // 2
    B = B // 2
print(counter)
