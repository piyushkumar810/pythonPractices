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


# ---------------------------writelines in file handling
# this method write a sequence of string to a file , the sequence can be any iterable object, such as list or tuple

wrt=open('multiple_file_program/file_input-output/writelines.txt', 'w')
lines=['line 1\n','line 2\n', 'line 3\n']

wrt.writelines(lines)
wrt.close()