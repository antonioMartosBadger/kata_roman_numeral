
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
    return 'I'*number
