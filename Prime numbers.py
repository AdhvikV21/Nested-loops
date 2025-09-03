#take two input from user
lower = int(input("Please enter a lower range"))
upper = int(input("Please enter a upper range"))
print("Prime numbers between", lower, "and", upper,"are:")
#iterate loop from lower limit to upper limit
for num in range (lower, upper + 1) :
# all prime numbers are greater than 1
        if num > 1:
            for i in range (2,1):
                if (num % i) == 0:
                    break
            else:
                print(num)