#Diego Mendez
def encode(toEncode):
    encoded = ""
    for i in toEncode:
        if int(i)<=6:
            encoded += str(int(i) + 3)
        elif int(i)>6:
            encoded += str(int(i) - 7)
    return encoded



if __name__ == '__main__':
    encoded_string = encode("01234567")
    decoded_string = decode("98765432")
