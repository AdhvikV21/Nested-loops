#take input of a work
string = input("Please enter your word:")
#take input of a character
char = input("Please enter your character")
i = 0
count = 0
# loop will to find the occurence of character
while(i < len(string)): # string operation
    if string [i] ==char: #condition 1
        count = count + 1
    i = i + 1

#Display the result
print("The total number of times,", char, "Has occured = ", count)
