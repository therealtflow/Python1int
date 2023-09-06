
n = 0
#for loop setting range of numbers
for i in range(1,6):
    while True:
        #try block that takes user input
        try:
            user = int(input("Enter a number: "))
            n += user
            break
        #stops user from entering a char or string
        except ValueError:
            print("Invalid input. Please enter a int.")
            continue

#prints sum of numbers entered by user
print("Your sum is",n)