# -----------------------------using truncate function in file handling
# if you want to specify size of the file then we can use truncate funcation 

with open('multiple_file_program/file_input-output/truncate.txt','w') as f:
    f.write('hello world3')
    f.truncate(5)

with open('multiple_file_program/file_input-output/truncate.txt','r') as f:
    print(f.read())