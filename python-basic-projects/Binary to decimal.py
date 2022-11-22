try:
    while(True):
        menu = int(input("Choose an option: \n 1. Decimal to binary \n 2. Binary to decimal\n 3. Exit \n Option: "))
        if menu < 1 or menu > 3:
            raise ValueError
        if menu == 1:
            dec = int(input("Input your decimal number:\nDecimal: "))
            print("Binary: {}".format(bin(dec)[2:]))
        elif menu == 2:
            binary = input("Input your binary number:\n Binary: ")
            print("Decimal: {}".format(int(binary, 2)))
        elif menu == 3:
            break
    pass
except ValueError:
    print ("please choose a valid option")