
def dec_to_bin():
    num = int(input("Enter a decimal number: "))

    if num == 0:
        print("Binary: 0")
        return

    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2

    print("Binary:", binary)

dec_to_bin()
