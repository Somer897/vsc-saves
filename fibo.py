n = int(input())
kol = 0
while n != 0:
    if n % 3 == 0:
        n = n - 3
    elif n % 3 == 1:
        n = n - 1
    elif n % 3 == 2:
        n = n - 2
    kol += 1
    print(kol)