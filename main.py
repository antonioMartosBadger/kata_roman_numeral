
UNIQUE_VALUES = {
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X'
}

def convert(number: int) -> str:
    if number in UNIQUE_VALUES:
        return UNIQUE_VALUES[number]
    else:
        return calculate_conversion(number)
        
def calculate_conversion(number: int) -> str:
    if number > 5:
        return 'V' + 'I'*(number-5)
    return 'I'*number
