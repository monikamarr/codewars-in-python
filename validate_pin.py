def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        for i in range(len(pin)):
            if not is_numeric(pin[i]):
                return False
        return True
    return False

def is_numeric(char):
    if  ord(char) >= 48 and ord(char) <=57:
        return True
    else:
        return False
