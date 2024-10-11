file = open('test.txt')
#read all the contents of file
#read n number of characters by passing parameter


# print(file.read())

#read one single line at a time readLine()
#print(file.readline())

#Print line by line using readline method

# line = file.readline()
#
# while line !="":
#     print(line)
#     line = file.readline()



#valores como lista

datafile = file.readlines()
print(datafile)
for i in datafile:
    if i.__contains__("cat"):
        break

file.close()

