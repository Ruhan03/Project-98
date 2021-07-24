def swapFileData():
    data_a = ""
    data_b = ""

    one = input("Enter the name of the 1st file: ")
    two = input("Enter the name of the 2nd file: ")
    
    a = open(two, 'r')
    data_a = a.read()

    b = open(one, 'r')
    data_b = b.read()

    print(data_b)
    print(data_a)

swapFileData()