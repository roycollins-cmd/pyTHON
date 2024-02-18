largest = -9999999999
counter = 0
while True:
    number = int(input("Enter number or enter -1 to stop:"))
    if number == -1:
        break
    counter += 1

    if number > largest:
        largest = number

if counter != 0:
    print("the largest number is, ", largest)
else:
    print("you haven't entered any number")