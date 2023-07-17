#Vivianne Everington

def encode(password):
    encoded_pswd = ""
    for digit in password:
        encoded_digit = str(int(digit) + 3)
        encoded_pswd += encoded_digit
    return encoded_pswd