class vegetable:
    def __init__(self,name,price):
        self.vegi=name
        self.rate=price

obj=vegetable('onion', 50)

obj.quantity=7
obj.no_of_bags=2

print(obj.quantity + obj.rate + len(obj.__dict__))


# explanation

# here is the problem
# print(obj.quantity + obj.rate + len(obj.__dict__))

# Here, we’re calculating and printing the result of obj.quantity + obj.rate + len(obj.__dict__).

# obj.quantity is 7
# obj.rate is 50
# len(obj.__dict__) gives the number of attributes in the obj instance.

# Let’s examine obj.__dict__:

# obj.__dict__ is a dictionary holding all the instance attributes and their values:

'''{'vegi': 'onion', 'rate': 50, 'quantity': 7, 'no_of_bags': 2}
There are 4 attributes ('vegi', 'rate', 'quantity', and 'no_of_bags'), so len(obj.__dict__) is 4.'''