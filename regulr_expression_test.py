import re

def validate_phone_numner(number):
    if not re.match(r'^01[016789][1-9]\d{6,7}$',number):
        return False
    return True

print(validate_phone_numner('01012341234'))

print(validate_phone_numner('01001231234'))

print(validate_phone_numner('010134123411'))

print(validate_phone_numner('0101341234'))




