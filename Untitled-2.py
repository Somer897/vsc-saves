import datetime
def bubble_sort(nums):
    swapped = True

    tics = 0                           #задаем кол-во итераций

    nums = list(nums)                       #чтобы работали реверсы
    for i in range(len(nums)):
        nums[i] = int(nums[i])

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
                print('Количество операций:', tics)
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
            tics += 1
        
start_time = datetime.datetime.now()                                                                            #начало времени запуска проги

random_list_of_nums = (input('Введите свой список: ')).split()          #создание списка
for i in range(len(random_list_of_nums)):
    random_list_of_nums[i] = int(random_list_of_nums[i])

end_time = datetime.datetime.now()                                                                               #конец времени запуска проги
print('Время выполнения кода: ', end_time - start_time)                                                          #вывод времени выполнения программы

print(bubble_sort(random_list_of_nums))                                     #вывод списка