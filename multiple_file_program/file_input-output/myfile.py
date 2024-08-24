# ------------------------------readline in file handling 
# readline() method is used to read a single line from the file . if we want to read multiple line in pyhton then we can use loop.
# the readlines() method is used to read all the lines of the file and returens them in the list

f=open('multiple_file_program/file_input-output/myfile.txt', 'r')
while True:
    line=f.readline()
    # print(line)
    if not line:
        break
    print(line)