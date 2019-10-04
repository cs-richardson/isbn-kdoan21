#Implement a program to validate ISBN-10 numbers.

userISBN = input("Input your ISPN: ")
isTrue = True
numSum = 0

for i in range(9):
    if 0 <= int(userISBN[i]) <= 9:
        numSum = numSum + int(userISBN[i]) * (10 - i)
    else:
        isTrue = False
		
if userISBN[9] != 'X' and 0 <= int(userISBN[9]) <= 9:
    isTrue = False

if userISBN[9] == 'X':
    numSum = numSum + 10
else:
    int(userISBN[9]) 

if numSum % 11 != 0:
    isTrue = False

if isTrue == True:
    print("Your ISBN is Valid.")
else:
    print("Your ISBN is Invalid.")
