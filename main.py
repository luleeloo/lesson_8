# Завдання 1 Написати рекурсивну функцію знаходження ступеня числа.
# def get_num_pow(number, degree):
#     if degree == 1:
#         return number
#     elif degree == 0:
#         return 1
#     elif degree < 0:
#         return 1 / get_num_pow(number, -degree)
#     else:
#         return number * get_num_pow(number, degree - 1)
#
#
# print(get_num_pow(7, 3))

# get_num_pow(7,3) -> 7 * get_num_pow(7, 2) => 343
# get_num_pow(7,2) -> 7 * get_num_pow(7, 1) => 49
# get_num_pow(7,1) -> 7 * get_num_pow(7, 0) => 7

# Завдання 2 Написати рекурсивну функцію, яка виводить N зірок у ряд, число N задає користувач.
# Проілюструйте роботу функції прикладом. (Протестувати)

def print_asterisks(N):
    if N > 0:
        print_asterisks(N - 1)
        print('*', end='')


try:
    N = int(input("Enter the number of asterisks you want to receive: "))
    print("Result:")
    if N > 0:
        print_asterisks(N)
    else:
        print("Wrong format: Please enter one positive number")
except ValueError:
    print("Wrong format: Please enter one positive number")

# if user inputs 5 (N=5)
# print_asterisks(5) -> print_asterisks(4)
# print_asterisks(4) -> print_asterisks(3)
# print_asterisks(3) -> print_asterisks(2)
# print_asterisks(2) -> print_asterisks(1)
# print_asterisks(1) -> *
# print_asterisks(2) -> *
# print_asterisks(3) -> *
# print_asterisks(4) -> *
# print_asterisks(5) -> *
# Result: *****
