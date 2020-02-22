import random
number = random.randint(1,40)
tries = input()
tries = int(tries)

print ("You have 5 guesses to find my number otherwise you lose")

while tries < 5:
    answer = int(input("Please enter a number between 1 and 40:"))
    if answer == number:
        break
    if answer > number:
        print ("Choose a number lower")
    if answer < number:
        print ("Choose a number higher")

    if tries > 5:
        print ("Sorry but you are out of tries!")
        print ("Better luck next time")

print ("Nice work you found my number")

