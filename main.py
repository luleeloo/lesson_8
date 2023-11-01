# # Завдання 1 Написати рекурсивну функцію знаходження ступеня числа.
# # def get_num_pow(number, degree):
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
#
# # як це працює:
# # get_num_pow(7,3) -> 7 * get_num_pow(7, 2)
# # get_num_pow(7,2) -> 7 * get_num_pow(7, 1)
# # get_num_pow(7,1) -> 7 * get_num_pow(7, 0) => 7
# # get_num_pow(7,2) -> 7 * get_num_pow(7, 1) => 49
# # get_num_pow(7,3) -> 7 * get_num_pow(7, 2) => 343
# # result: 343

# # Завдання 2 Написати рекурсивну функцію, яка виводить N зірок у ряд, число N задає користувач.
# # Проілюструйте роботу функції прикладом. (Протестувати)

# def print_asterisks(N):
#     if N > 0:
#         print('*', end='')
#         print_asterisks(N - 1)
#
#
# try:
#     M = int(input("Enter the number (<= 10) of asterisks you want to receive: "))
#     print("Result:")
#     if 0 < M <= 10:
#         print_asterisks(M)
#     else:
#         print("Wrong format: Please enter one positive number (<= 10)")
# except ValueError:
#     print("Wrong format: Please enter one positive number (<= 10)")
#
# # як це працює:
# # if user inputs 5 (N=5)
# # print_asterisks(5) => * -> print_asterisks(4)
# # print_asterisks(4) => * -> print_asterisks(3)
# # print_asterisks(3) => * -> print_asterisks(2)
# # print_asterisks(2) => * -> print_asterisks(1)
# # print_asterisks(1) => *
# # Result: *****


# # Завдання 3 Написати рекурсивну функцію, яка обчислює суму всіх чисел у діапазоні від a до b.
# # Користувач вводить a та b. Проілюструйте роботу функції прикладом.

# def sum_of_numbers(a, b):
#     if a == b:
#         return a
#     elif a < b:
#         return a + sum_of_numbers(a + 1, b)
#     else:
#         return b + sum_of_numbers(a, b + 1)
#
#
# def get_input():
#     try:
#         c = int(input("Enter the first number: "))
#         d = int(input("Enter the last number: "))
#         if 0 <= c <= 10 and 0 <= d <= 10:
#             return c, d
#         else:
#             print("Error: Both numbers must be <= 10. Try again, please.")
#             return get_input()
#     except ValueError:
#         print("Wrong format: Please enter a positive number, which is <= 10")
#         return get_input()
#
#
# e, f = get_input()
# if e > f:
#     e, f = f, e
# result = sum_of_numbers(e, f)
# print(f"Sum of numbers from {e} to {f} is {result}")
#
# # як це працює:
# # if user inputs numbers 3 and 6:
# # sum_of_numbers(3, 6) -> 3 + sum_of_numbers(4, 6)
# # sum_of_numbers(4, 6) -> 4 + sum_of_numbers(5, 6)
# # sum_of_numbers(5, 6) -> 5 + sum_of_numbers(6, 6)
# # sum_of_numbers(6, 6) => 6
# # sum_of_numbers(5, 6) -> 5 + sum_of_numbers(6, 6) => 11
# # sum_of_numbers(4, 6) -> 4 + sum_of_numbers(5, 6) => 15
# # sum_of_numbers(3, 6) -> 3 + sum_of_numbers(4, 6) => 18
# # result: 18
# # all tasks done
