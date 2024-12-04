# my_lib.py

# Функция для генерации n чисел Фибоначчи
def fibonacci(n):
    """Возвращает список из n чисел Фибоначчи"""
    if n <= 0:
        raise ValueError("Число n должно быть больше нуля.")
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

# Функция сортировки пузырьком
def bubble_sort(arr):
    """Возвращает отсортированный список методом пузырька"""
    sorted_arr = arr[:]
    n = len(sorted_arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if sorted_arr[j] > sorted_arr[j+1]:
                sorted_arr[j], sorted_arr[j+1] = sorted_arr[j+1], sorted_arr[j]
    return sorted_arr

# Калькулятор
def calculator(a, b, operation):
    """Выполняет арифметическое действие и возвращает результат"""
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b == 0:
            raise ZeroDivisionError("Деление на ноль невозможно.")
        return a / b
    else:
        raise ValueError("Неверный знак операции.")
