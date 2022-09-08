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


print(power_numbers(1, 2, 5, 7))


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
    if num % 2:
        return True
    else:
        return False


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def filter_numbers(numbers, filter_type):
    if filter_type == ODD:
        ff = is_odd
    elif filter_type == EVEN:
        ff = is_even
    elif filter_type == PRIME:
        ff = is_prime
    else:
        print('It\'s unknown filter type')
        return

    return list(filter(ff, numbers))


print('even numbers  =', filter_numbers(range(0, 50), EVEN))
print('odd numbers   =', filter_numbers(range(0, 50), ODD))
print('prime numbers =', filter_numbers(range(0, 50), PRIME))