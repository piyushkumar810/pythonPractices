class Apple:
    def one(self):
        return self.two()
    
    def two(self):
        return 'Apple'
    
class boy(Apple):
    def two(self):
        return 'boy'
    
b=boy()
print(b.two())