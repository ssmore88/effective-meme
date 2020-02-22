import random

print ("Play Slay the Dragon?")
answer = input("Yes or no?")

if answer.lower() == "yes":
    print ("Very well let's get started")
else:
    quit()

name = input("Enter Your Name:")
print ("Well" ,name ,"your first opponent is spitball")

print ("Here's how the game works, you have three attacks Charge, Punch, Shoot")
print ("Charge does 15 damage")
print ("Punch does 5 damage")
print ("Shoot does 10 damage")
print ("You can only use your all attacks unlimitedely ")

text = input("Do you understand? yes or no:")
if text.lower() == "yes":
    print ("Good! Now your opponent has 30 damage and you have 40 beat him and we'll talk more. I have to leave!")

x = 30
y = 40

while True:
    answer1 = input("Your turn which move would you like to execute:") #import rand for critical attack
    if answer1.lower() == "charge":
        print ("Nice shot you did 15 damage. Spitball now has" ,x - 15.)
        x = x - 15
    if answer1.lower() == "punch":
        print ("Nice shot you did 5 damage. Spitball now has" ,x - 5.)
        x = x - 5
    if answer1.lower() == "shoot":
        print ("Nice shot you did 10 damage. Spitball now has" ,x - 10.)
        x = x - 10

    if x <= 0:
        print("Great work" ,name , "you have beaten your first opponent.")
        break
    if y <= 0:
        print("You Lost")
        break

    comp_charge = random.randint(1,3) * 5  # either a 5 , 10 , 15
    if comp_charge == 5 :
        comp_charge_as_string = "punch"
    if comp_charge == 10 :
        comp_charge_as_string = "shoot"
    if comp_charge == 15 :
        comp_charge_as_string = "charge"

    #print (comp_charge)
    print ("Your turn is over now it is spitball's turn")
    print ("spitball has executed " ,comp_charge_as_string , "to you.")
    print ("Now you have" ,y - comp_charge ,"damage left.")
    y = y - comp_charge

print ("Hey" ,name , "great win today. I knew you could do it, but sadly spitball was only a minion to the next monster you have to beat. I know you probably have a lot on you mind but to clear somethings up my name is Avachai. I am an ancient god who has lost all of his power fighting Draco, please beat him in combat and I will be free, I can guard the world again!")
answer3 = input("I have located him in an acient valley across the Himalayas he expects you there, would you like to fight Draco:")

if answer3.lower() == 'yes':
    print ("Very well looks like you get to attack first and also I added 10 HP to your health bar it was the only energy I have left")
else:
    quit()

x1 = 50
y1 = 50

while True:
    answer4 = input("Which move would you like to execute:") #import rand for critical attack
    if answer4.lower() == "charge":
        print ("Nice shot you did 15 damage. Spitball now has" ,x1 - 15.)
        x1 = x1 - 15
    if answer4.lower() == "punch":
        print ("Nice shot you did 5 damage. Spitball now has" ,x1 - 5.)
        x1 = x1 - 5
    if answer4.lower() == "shoot":
        print ("Nice shot you did 10 damage. Spitball now has" ,x1 - 10.)
        x1 = x1 - 10
        
    if x1 <= 0:
        print("Great work" ,name , "you have beaten Draco.")
        break
    if y1 <= 0:
        print("You Lost")
        quit()

    draco_charge = random.randint(1,4) * 5  # either a 5, 10, 15, 20
        comp_charge_as_string = "punch"
    if comp_charge == 10 :
        comp_charge_as_string = "shoot"
    if comp_charge == 15 :
        comp_charge_as_string = "charge"
    if comp_charge == 20 :
        comp_charge_as_string = "critical attack"

    print ("Your turn is over now it is spitball's turn")
    print ("spitball has executed " ,comp_charge_as_string , "to you.")
    print ("Now you have" ,y1 - comp_charge ,"damage left.")
    y1 = y1 - comp_charge
