def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n - 1)


def IsPalindrome(S):
    if len(S) <= 1:
        return True
    else:
        return S[0] == S[-1] and IsPalindrome(S[1:-1])
    

def Sum(A):
    if len(A) == 0:
        return 0
    else:
        return Sum(A[:-1]) + A[-1]
    

def Max(A):
    if len(A) == 1:
        return A[0]
    else:
        return max(Max(A[:-1]), A[-1])
    

def Fib(n):
    if n <= 1:
        return n
    else:
        return Fib(n - 1) + Fib(n - 2)
    

def power(a, n):
    if n == 0:
        return 1
    elif n % 2 == 1:
        return power(a, n - 1) * a
    else:
        return power(a, n // 2) ** 2
    

def move(n, start, finish):
    if n == 1:
        print("Перенести диск 1 со стержня", start, "на стержень", finish)
    else:
        temp = 6 - start - finish # Вспомогательный колышек
        move(n - 1, start, temp)
        print("Перенести диск", n, "со стержня", start, "на стержень", finish)
        move(n - 1, temp, finish)
# Для решения головоломки из 10 дисков вызываем так:
move(10, 1, 3)


def move(n, start, finish):
    if n > 0:
        temp = 6 - start - finish # Вспомогательный колышек
        move(n - 1, start, temp)
        print("Перенести диск", n, "со стержня", start, "на стержень", finish)
        move(n - 1, temp, finish)


import sys
sys.setrecursionlimit(10000)

def factorial_iterative(num):
    factorial = 1
    if num < 0:
        print("Факториал не вычисляется для отрицательных чисел")
    else:
        for i in range (1, num + 1):
            factorial = factorial*i
        print(f"Факториал {num} это {factorial}")

factorial_iterative(10)