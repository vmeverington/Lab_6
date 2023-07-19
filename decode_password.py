# Megan Ritchie

def decode(password):
    decoded_pass = ""
    for i in password:
        decoded_pass += str(int(i) - 3)
    return decoded_pass
