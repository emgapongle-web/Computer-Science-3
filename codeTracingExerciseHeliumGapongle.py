#Code #1
def greet_students(name, nChar):
    for i in range(min(nChar, len(name))):
         print(name[i])
        

name = input("Enter a Name: ")
nChar = input("Enter any numeric number: ")
nChar = int(nChar)
greet_students(name, nChar)

#a. If the name is “Joseph The Dreamer” and nChar is 5, the output of the code above 
#would be "Josep" with each character displayed in separate lines.

#b. Using the same name and nChar is 20, the output would be 
#"Joseph The Dreamer" with each character displayed in separate lines.

#c. I would add min and len so that 
#it would print the actual length of the string.

#Code #2
def greet_students(name, nChar):
    for i in range(nChar, 0, -1):
         print(name[0 : i])

name = input("Enter a name ")
greet_students(name, len(name))

#a. the error is that in printing the name, 
#the amount of letters dont decrease
#I then modified the for statement and the print statement

#b. Modified the for statement and the print statement.

#Code #3
def sum_of_squared(n):
    total = 0

    for i in range(1, n + 1):
        total += i**2

    return total
n = 0 
while n < 1 or n > 100:
    n = input("Enter a Number from 1 to 100: ")
    n = int(n)

print("Sum of all squared numbers is", sum_of_squared(n))