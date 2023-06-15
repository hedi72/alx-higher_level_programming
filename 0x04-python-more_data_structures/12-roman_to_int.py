def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    length = len(roman_string)
    
    for i in range(length):
        if i < length - 1 and roman_values[roman_string[i]] < roman_values[roman_string[i+1]]:
            total -= roman_values[roman_string[i]]
        else:
            total += roman_values[roman_string[i]]
    
    return total
