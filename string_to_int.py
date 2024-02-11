# Given a string, convert it to an integer without using the builtin str function. 
# You are allowed to use ord to convert a character to ASCII code.

# Consider all possible cases of an integer. 
# In the case where the string is not a valid integer, return None.

def convert_to_int(s):
    if not s:
        return None
    pwr = len(s) - 1
    total = 0
    for ch in s:
        ch_val = ord(ch) - ord('0')
        if ch_val > ord('9') - ord('0'):
            return None
        total += ch_val * (10 ** (pwr))
        pwr -= 1
    return total

# test case 1
print(convert_to_int('103'))
# test case 2
print(convert_to_int(''))
# test case 3
print(convert_to_int('as9'))


