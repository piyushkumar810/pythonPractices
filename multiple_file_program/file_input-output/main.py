# ------------------------------file I/O in python

# f=open('multiple_file_program/file_input-output/mainfile.txt','r')
# print(f)

# text=f.read()
# print(text)
# f.close()

# writing to a file
# g=open('multiple_file_program/file_input-output/mainfile2.txt', 'w')
# text=g.write("hello world")
# print(text)
# g.close()

# appending a file
h=open('multiple_file_program/file_input-output/mainfile2.txt', 'a')
text=h.write(" hello world")
h.close()

# the use of "with" statement --> we dont have to close the file everytime 