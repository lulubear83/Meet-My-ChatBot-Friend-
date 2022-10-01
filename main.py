import time

#Meet my Chatbot Friend Starter Code

#Chatbot introduces them self
print("Hello! I'm Penelope the chatbot.\n")
name = input("What's your name? ")

print("Let's see if I can spell that:")
time.sleep(2)

#Add Part 5 code here
name_list = list(name)
print(name_list)
time.sleep(2)

for letter in name_list:
    print(letter)
    time.sleep(1)

print("\nNice to meet you " + name)
time.sleep(1)

#Chatbot asks questions
print("\nCan you tell me about yourself?\n")

#add Part 2 Step 2 code in this section
print("Where are you from?")
place = input("You are from...")
print("I'd love to visit " + place + " one day!")

print("\nWhat are you passionate about?")
passion = input("You are passionate about... ")
print("whoa, that's amazing " + passion + " it sounds cool!")

print("\nWhat is your personal goal?")
goal = input("You hope to... ")
print("I really admire your goal to " + goal + " \nI now you can do it :)`")

#Chatbot tells their story
#add Part 4 code here
while True:
    topic = input(
        "\nWhat would you like to know about me? - home, passion, goal, or none?\n"
    )

    #add Part 3 code here
    if topic.lower() == "home":
        print(
            "I come from a chilly cave \nin the National Park. \nIt's just south of the turnpike, \nmake a right on Apple Orchard Way. \nahhhh-hhaaaaaa"
        )

    elif topic.lower() == "passion":
        print(
            "I enjoy \nahhhh-hhaaaaaa \nOh excuse my yawning. \nI enjoy reading about sleep studies \nor the noctural habits of squirrels \nwhen I'm not sleeping, \nof course."
        )

    elif topic.lower() == "goal":
        print(
            "There's a sleep competition this October and \nI need to prepare.  \nAs soon as I find my binky though. \nI think I left it at my mom's cave."
        )

    elif topic.lower() == "none" or topic.lower() == "nothing":
        print("Oh, okay.")
        break

    else:
        print("Sorry, I didn't catch that.")

#Guess Favorite Color
while True:
    color = input("\nCan you guess if my favorite is red, green or blue? \n")

    if color.lower() == "green":
        print("Whoa, You're good, Yes, my favorite color is green")
        break

    elif color.lower() == "blue":
        print("Nice try, guess again.\n")

    elif color.lower() == "red":
        print("No. Not red, but keep guessing. \n")

    else:
        print("That was not an option, try again.")

print(
    "Alll right then. \nGuess, I'll see you around. \nIf you're ever on Apple Orchard Way, stop by and say hi"
)
