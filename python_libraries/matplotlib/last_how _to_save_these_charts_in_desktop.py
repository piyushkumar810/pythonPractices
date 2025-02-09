# ------------------- How to save these charts in your desktop using matplotlib

import matplotlib.pyplot as plt

brands = ["OnePlus", "Apple", "Vivo", "Redmi", "Samsung"]
users = [13, 25, 22, 18, 22]

ex=[0,0.1,0,0,0]

plt.figure(figsize=(7, 7))  # Set figure  size
plt.pie(users, labels=brands, autopct="%1.1f%%", startangle=140, colors=["red", "blue", "green", "orange", "purple"], explode=ex, shadow=True)
plt.title("Market Share of Smartphone Brands")

# plt.savefig -> this is used to save the figure, 
                 # this contains lots of attribute like : pad_inches= 0.7, bbox_inches="tight" and more ...
plt.savefig("pie.png")

plt.show()