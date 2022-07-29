
UNIQUE_VALUES = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M'
}

def convert(number: int) -> str:
    # converted_number = ""
    # for val in UNIQUE_VALUES:
    #     #if number - val == 0:
    #         #converted_number += UNIQUE_VALUES[val]
    #     if number - val % 10 == 0:
    #         converted_number += UNIQUE_VALUES[val] #+ convert(number - val)

    if number in UNIQUE_VALUES:
        return UNIQUE_VALUES[number]
    elif is_direct_subtraction(number):
        return return_direct_subtraction(number)
    else:
        return calculate_conversion(number)
        
def calculate_conversion(number: int) -> str:
    if number > 10:
        return 'X' + convert(number - 10)
    if number > 5:
        return 'V' + convert(number-5)
    return 'I'*number

def is_direct_subtraction(number: int) -> str:
    result = False
    for key_1, value_1 in UNIQUE_VALUES.items():
        for key_2, value_2 in UNIQUE_VALUES.items():
            if number == key_1 - key_2:
                result = True
            if number == key_2 - key_1:
                result = True
    return result


def return_direct_subtraction(number: int) -> str:
    for key_1, value_1 in UNIQUE_VALUES.items():
        for key_2, value_2 in UNIQUE_VALUES.items():
            if number == key_1 - key_2:
                return value_2 + value_1
            if number == key_2 - key_1:
                return value_1 + value_2
