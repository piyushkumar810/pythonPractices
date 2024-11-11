def display_persion(**args):
    for i in args:
        print(i,end='')

display_persion(name="piyush", age=22)

''' here you will think how args can take argument in key-value pair but you are not seeing properly in parameter 
before args there is two astric (**) this indicate that it is not args it is kwargs'''