from encode_password import encode
from decode_password import decode

if __name__ == "__main__":
    while True:
        print("\nMenu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
    
        option = input("Please enter an option: ")
    
        if option == "1":
            pswd = input("Please enter your password to encode: ")
            encoded_pswd = encode(pswd)
            print("Your password has been encoded and stored!")
      
        elif option == "2":
            print("The encoded password is " + encoded_pswd + ", and the original password is " + decode(encoded_pswd) + ".")
      
        elif option == "3":
            exit()