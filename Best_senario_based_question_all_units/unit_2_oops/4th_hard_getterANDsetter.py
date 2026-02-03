'''
📌 Scenario
You are designing an Online Movie Ticket Booking System.
For security and correctness:
Ticket price must NOT be accessed directly
Ticket price must always be greater than 0
Ticket price can be read but modified only with rules
Any invalid price update must be rejected

📝 WHAT YOU HAVE TO DO
1️⃣ Create a class MovieTicket
2️⃣ Attributes
movie_name → public
__price → private

3️⃣ Methods you MUST create
get_price()
set_price(new_price)
display_ticket()

4️⃣ Rules you MUST enforce
__price must never be accessed directly
Price update allowed only if new_price > 0
If invalid price is given → print error message
display_ticket() must use the getter

5️⃣ Object creation & usage
Create one object
Display ticket details
Update price with a valid value
Update price with an invalid value
Display ticket details again
❌ Don’t ask how
❌ Don’t copy old code
✔ Apply encapsulation properly
✔ Use getter & setter correctly
'''
class MovieTicket:
    def __init__(self, movie_name, price):
        self.movie_name = movie_name
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
            print("Ticket price updated successfully")
        else:
            print("Invalid price of ticket")

    def display_ticket(self):
        print(f"Movie name: {self.movie_name}")
        print(f"Final ticket price: {self.get_price()}")

MT=MovieTicket("Marut mera dost",1001)
MT.display_ticket()
print()

MT.set_price(1501)
MT.display_ticket()
print()

MT.set_price(0)
MT.display_ticket()

