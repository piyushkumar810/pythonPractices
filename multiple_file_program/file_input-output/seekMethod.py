# ---------------------seek() Method AND tell() Method
# seek method allows you to move the current position within the file

with open('multiple_file_program/file_input-output/seekMethod.txt','r') as f:
    print(type(f))

    # move to the 10 byte in the file 
    f.seek(10)

    # f.tell() --> simpley tells your current position in the file
    print(f.tell())

    # read the next 5 byte
    data=f.read(5)
    print(data)

    print(f.tell())