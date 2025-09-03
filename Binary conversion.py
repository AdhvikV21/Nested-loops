num = float(input("Please enter a decimal number: "))
binary_string = ""
if num == 0:
    binary_string = "0"
while num > 0:
    rem = num % 2
    binary_string = str(rem) + binary_string
    num = num // 2
print("Binary representation:", binary_string)


