"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    square_of_num = []
    for num in numbers:
        num = num ** 2
        square_of_num.append(num)
    return square_of_num


print('power_numbers =', power_numbers(1, 2, 5, 7))

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(num):
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


def is_odd(num):
    return num % 2


def is_even(num):
    return num % 2 == 0


def filter_numbers(numbers, filter_type):
    dict_filter = {ODD: is_odd,
                   EVEN: is_even,
                   PRIME: is_prime,
                   }
    return list(filter(dict_filter[filter_type], numbers))


print('even numbers  =', filter_numbers(range(0, 50), EVEN))
print('odd numbers   =', filter_numbers(range(0, 50), ODD))
print('prime numbers =', filter_numbers(range(0, 50), PRIME))
