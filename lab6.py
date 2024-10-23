#Diego Mendez
def encode(encode):
    encoded = ""
    for i in encode:
        if int(i)<=6:
            encoded += str(int(i) + 3)
        elif int(i)>6:
            encoded += str(int(i) - 7)
    return encoded



def main():
    option = None
    encoded = None
    while True:
        print("-------------\n1. Encode\n2. Decode\n3. Quit\n")
        option = input("Please enter an option: ")
        if option == "1":
            encoded  = encode(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!\n")
        elif option == "2":
            print(f'The encoded password is {encoded}, and the original password is {decode(encoded)}\n')
        elif option == "3":
            break

if __name__ == '__main__':
    main()


