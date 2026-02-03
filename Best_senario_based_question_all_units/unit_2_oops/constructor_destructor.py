class Sample:
    def __init__(self):
        print("Constructor called: Object is created")

    def __del__(self):
        print("Destructor called: Object is destroyed")


# creating object
obj = Sample()

# deleting object
del obj
