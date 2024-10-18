class employee:
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return f"the anme of employee is {self.name} from str"

    def __repr__(self):
        return f"the name of employee is {self.name} from repr"

    def __call__(self):
        print("hey i am good")