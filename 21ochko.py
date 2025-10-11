import random
start = 2
end = 10
money = 10000
invent = 0
inventor1 = 0
choice = int(input('Хотите играть? Да(1)'))
while money>0:
    print('Ваш счёт:', money)
    stavka = int(input('Какова ваша ставка?: '))               #Ставка
    if stavka > money:
        print('Ты даун?')
        money -= 100
        print('Дауны платят компенсацию в размере 100 рублей')
    else:
        if choice == 1:
            invent = random.randint(start, end)            #Инвентарь
            random1 = random.randint(start, end)
            invent += random1
            print('Ваши карты:', invent)
            game1 = int(input('Хотите ещё карт? Да(1)/Нет(2)'))
            while game1 == 1:
                random3 = random.randint(start, end)
                invent += random3
                print('Ваши карты:', invent)
                if invent < 21:
                    game1 = int(input('Хотите ещё карт? Да(1)/Нет(2)')) 
                else:
                    game1 = 2
        else:
            print('Error')
        inventor1 = random.randint(start, end)            #Инвентарь pc
        random1 = random.randint(start, end)
        inventor1 += random1
        while inventor1 <16:
            random2 = random.randint(start, end)
            inventor1 += random2
            inventor1 = inventor1
        if invent <= 21:                        #Вывод итогов
            if inventor1 <= 21:
                if invent > inventor1:
                    if invent == 21:
                        print('У противника: ', inventor1)
                        print('Блэкджек! Поздравляем!')
                        money += (stavka * 2)
                    else:
                        print('У противника: ', inventor1)
                        print('Поздравляем!')
                        money += stavka
                elif invent < inventor1:
                    print('У противника: ', inventor1)
                    print('Ты проебал')
                    money -= stavka
                else:
                    print('У противника: ', inventor1)
                    print('Ничья!')
                    money = money
            else:
                print('У пк перебор, вы победили!')
                money += stavka
        else:
            print('Перебор')
            money -= stavka
input('Ебать ты лошара!')