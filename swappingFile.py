def swapFileData():

    textFile1 = input("Enter the first file's name: ")
    textFile2 = input("Enter the second file's name: ")

    read_a = open(textFile1, 'r')
    data_a = read_a.read()

    read_b = open(textFile2, 'r')
    data_b = read_b.read()

    write_a = open(textFile1, 'w')
    write_a.write(data_b)

    write_b = open(textFile2, 'w')
    write_b.write(data_a)

swapFileData()