number1 = float(input("Введите первое число: "))
number2 = float(input("Введите второе число: "))

print('Выберите операцию:')

print('1.Сложение')
print('2.Разность')
print('3.Умножение')
print('4.Деление')
print('5.Возведение в степень')

choice = int(input("\nОперация: "))

match choice:
    case 1:
        print(f"{number1} + {number2} = {number1 + number2} ")
    case 2:
        print(f"{number1} - {number2} = {number1 - number2} ")
    case 3:
        print(f"{number1} * {number2} = {number1 * number2} ")
    case 4:
        print(f"{number1} - {number2} = {number1 / number2} ")
    case 5: 
        print(f"{number1} ^ {number2} = {number1 ** number2} ")
    case _:
        print('Error')
input('\n\n Нажмите "Enter", чтобы выйти')