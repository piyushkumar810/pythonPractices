from abc import ABC, abstractmethod

class vechicle(ABC):
    def __init__(self,n):
        self.no_of_types=n

    @abstractmethod
    def start(self):
        pass

    def display(self):
        print("hi i am calling from vechicle class")