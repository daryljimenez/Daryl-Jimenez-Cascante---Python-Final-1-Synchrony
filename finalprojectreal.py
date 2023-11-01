print("Hey, let me survey you on your ability to survive a zombie apocalypse with my questionnaire!")

# List, provides the program with the questions that are going to be asked throughout the execution of the program.

# This stores queries.
questionList = [
    "Let us now begin with the first question: Are you capable of starting fires?",
    "Do you possess experience with armed and melee weapons?",
    "How about construction? Know how to build to any extent?",
    "Are you capable of reading maps?",
    "Are you a seasoned rock climber?",
    "Are you a particularly fit individual?",
    "And, the last question: Can you hunt or fish?",
]

# This stores responses to user interactions.
correctAnswerList = [
    "Nice response! Alright, let's move on!",
    "Wow, that’s phenomenal! Next question.",
    "That’ll definitely come in handy!",
    "Whew! Now that’s insane!",
    "That is truly impressive!",
    "Yeah, that’s pretty useful!",
    "Foraging for food is quite useful.",
]

# This stores responses to user interactions.
incorrectAnswerList = [
    "Aw dang it!",
    "Interesting. Let us move on.",
    "Err, maybe try looking at some maps at some time!",
    "Can’t get them all, am I right?",
    "Eesh, I wish you luck!",
    "Dang, couldn’t meet the mark!",
]

def finalDeclaration():
    print(f"You scored {scoreVar} points!")

# This is a variable that stores a number indicative of a particular response within the correct answer list.
correctAnswerQuantified = 0

# This is a variable that stores a number indicative of a particular response within the incorrect answer list.
incorrectAnswerQuantified = 0

# This variable stores the score of the player.
scoreVar = 0

# Introducing the boolean variable to control the loop.
survivalSkills = True

# This here ascertains that the user is provided a question after each response.
for question in questionList:
    if not survivalSkills:
        break

    userAnswerVar = input(question + " (Yes/No)?: ")

    if userAnswerVar.lower() == "yes":
        scoreVar += 1
        correctAnswerQuantified += 1

        # This either breaks or continues the string.
        if correctAnswerQuantified >= 7:
            break
        else:
            print(correctAnswerList[correctAnswerQuantified])

    elif userAnswerVar.lower() == "no":
        scoreVar += 0
        incorrectAnswerQuantified += 1

        # This either breaks or continues the string.
        if incorrectAnswerQuantified >= 7:
            break
        else:
            print(incorrectAnswerList[incorrectAnswerQuantified])

# This function is declared once the loop is exited.
finalDeclaration()
