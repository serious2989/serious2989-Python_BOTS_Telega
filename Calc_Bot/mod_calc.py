def sum_data(num_1, num_2):
    return num_1 + num_2


def sub_data(num_1, num_2):
    return num_1 - num_2


def mul_data(num_1, num_2):
    return num_1 * num_2


def div_data(num_1, num_2, par="/"):
    if num_2:
        if par == "%":
            return num_1 % num_2
        elif par == "//":
            return num_1 // num_2
        return num_1 / num_2
    else:
        return "Деление на 0!"


def pow_data(num_1, num_2=None):
    if not num_2:
        return num_1 ** 0.5
    return num_1 ** num_2
