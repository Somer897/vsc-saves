from random import randint as r 

x = list(range(1, 10_000_000))
jump = 1
isk = r(1, 10_000_000)
print(isk)
index = 0
is_found = False
i = 0
n = len(x)
k = 0

while jump < n and x[jump] <= isk:               #1 заход
        jump *= 2

left = jump // 2                 #деление нацело 5001 // 2 = 2500
right = min(jump, n - 1)          # 1 - если нашли элемент, 2 - если вышли за список
while left <= right:
    mid = left + (right - left) // 2             # 2500 + (3000-2500) //2 = 2750 
    if x[mid] == isk:                            # if 2750 = iskomoe
        index = mid
        is_found = True
        break                                   # vihod nahui

    elif x[mid] < isk:
        left = mid + 1
        k += 1

    else:
        right = mid - 1
        k += 1

if is_found is True:
    print(index)
    print(k)
else:
    print("Not found")
