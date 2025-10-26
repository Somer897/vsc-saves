def bubble_sort(nums):
    swapped = True

    nums = list(nums)                       #чтобы работали реверсы
    for i in range(len(nums)):
        nums[i] = int(nums[i])

    n = 0                                      #параметры для сравнения
    k = 0

    while swapped:
        for i in range(len(nums) - 1):                #цикл для смен

            n = 0                             #обновление переменных для новой итерации
            k =0

            for i in range(len(nums) - 1):               #счетчик инверсий обычного списка
                if nums[i] > nums[i + 1]:
                    n +=1

            if k == 0:           #чтобы в конце вернуть список к исходу (лишь для след операции)
                nums.reverse()
                for i in range(len(nums) - 1):                 #счетчик обратного списка
                    if nums[i] < nums[i + 1]:
                        k += 1
                nums.reverse()
            
            if n == 0:                               #если инверсии кончились
                swapped = False
                return nums

            elif n >= k:                                     #меняем местами если в ту сторону больше инверсий
                for i in range(len(nums) - 1):
                    if nums[i] > nums[i + 1]:
                        nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

            elif k > n:                                     #меняем, если в обратную сторону больше инверсий
                nums.reverse()
                for i in range(len(nums) - 1):
                    if nums[i] < nums[i + 1]:
                        nums[i], nums[i + 1] = nums[i + 1], nums[i]
                nums.reverse()
                swapped = True

random_list_of_nums = [5, 2, 1, 8, 4]
print(bubble_sort(random_list_of_nums))
