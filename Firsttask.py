try:

    file1 = open('sample.txt','r')
    reading_file = file1.read()

    print("Reading file content:\n" ,reading_file)

    file1.close()
except:
    print("Error: The file 'sample.txt' was not found.")
