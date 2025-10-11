number1 = float(input("Введите первое число: "))
number2 = float(input("Введите второе число: "))

print('Выберите операцию:')

print('1.Сложение')
print('2.Разность')
print('3.Умножение')
print('4.Деление')
print('5.Возведение в степень')

choice = input("\nОперация: ")

if choice == '1':
  print(f"{number1} + {number2} = {number1 + number2} ")
elif choice == '2':
  print(f"{number1} - {number2} = {number1 - number2} ")

elif choice == '3':
  print(f"{number1} * {number2} = {number1 * number2} ")

elif choice == '4':
  if number2 != 0:
   print(f"{number1} / {number2} = {number1 / number2} ")
  else: print('Error')

elif choice == '5':
  print(f'{number1} ^ {number2} = {number1 ** number2} ')
  
else: print('Неверное значение')
input('\n\n Нажмите "Enter", чтобы выйти')
