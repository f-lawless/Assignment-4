try:
    file1 = open("sample.txt", 'r')
    read_file = file1.readlines()
    #I have used the for loop so that no matter how many lines the file contains,
    # it prints all of them with their line number
    for i in range (0,len(read_file)):
        print("Line",i+1,':',read_file[i],end="")
    file1.close()
except FileNotFoundError:
    print("Error: The file named 'sample.txt.txt' was not found.")