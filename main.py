# Завдання 1 Написати рекурсивну функцію знаходження ступеня числа.
def get_num_pow(number, degree):
    if degree == 1:
        return number
    elif degree == 0:
        return 1
    elif degree < 0:
        return 1 / get_num_pow(number, -degree)
    else:
        return number * get_num_pow(number, degree - 1)


print(get_num_pow(7, 3))

# get_num_pow(7,3) -> 7 * get_num_pow(7, 2) => 343
# get_num_pow(7,2) -> 7 * get_num_pow(7, 1) => 49
# get_num_pow(7,1) -> 7 * get_num_pow(7, 0) => 7
