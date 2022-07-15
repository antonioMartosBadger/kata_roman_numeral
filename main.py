
UNIQUE_VALUES = {
    1: 'I',
    5: 'V'
}

def convert(number: int) -> str:
    if number in UNIQUE_VALUES:
        return UNIQUE_VALUES[number]
    else:
        return calculate_conversion(number)
        
def calculate_conversion(number: int) -> str:
    if number == 4:
        return 'IV'
    elif number > 5:
        return 'V' + 'I'*(number-5)
    return 'I'*number
