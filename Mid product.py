#input a number
num = int(input("Enter a number"))
t = num
numLen = 0
#iterate the loop
while t > 0:
    numLen = numLen + 1
    t = int(t/10)
if numLen > 4: #condition 1
    numLen = int(numLen/2)
    chk = 0
    while num > 0: # iterate the loop
        rem = num%10
    if chk == numLen: #nested condition 1
        midOne = rem
    elif chk == (numLen-1):
        midTwo = rem
    num = int(num/10)
    chk = chk + 1