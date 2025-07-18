print("Welcome to my quiz!")

Lives = 3

def askQuestion(q, a, le, li):
    level = le
    life = li
    while level == le:
        answer = input(q + " ")
        if answer.lower() == a:
            print("Correct!")
            level = level + 1
        else:
            life = life - 1
            print("Try again turkey! You have {} lives left".format(life))
            if life == 0:
                quit("You lost! Hit the green play button to play again.")
    return life

Playing = input("Are you going to play? ")
if Playing.lower() != "yes":
    quit("Bye bye!")

print("Ok let's play!")
print("first question.")

Lives = askQuestion("Which fruit did female wasps die in?", "figs", 1, Lives)

print("second question.")

Lives = askQuestion("How many eyes does a mantis have?", "five", 2, Lives)

print("third question.")

Lives = askQuestion("What is the tallest tree on earth?", "redwood", 3, Lives)

print("fourth question.")

Lives = askQuestion("What is the only country that is also a continent?", "australia", 4, Lives)

print("fifth question.")

Lives = askQuestion("What part of the human body contains the smallest bones?", "ear", 5, Lives)

print("sixth question.")

Lives = askQuestion("What social media platform is represented by a blue bird?", "twitter", 6, Lives)

print("last question.")

Lives = askQuestion("What is the currency of Japan?", "yen", 7, Lives)

print("Good job you passed my quiz! You lost {} lives.".format(3-Lives))