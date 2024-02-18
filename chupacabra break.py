placeholder = "chupacabra"
word = input("enter a word: ")

while word != placeholder:
    if word == placeholder:
        break
    word = input("enter word: ")

print("You have successfully left the loop!")