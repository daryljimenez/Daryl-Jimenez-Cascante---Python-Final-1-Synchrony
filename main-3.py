print("Hey, let me survey you on your ability to survive a zombie apocalypse with my questionaire!")

#List, provides the program with the questions that are going to be asked throughout the execution of the program. 

#This stores queries.
questionList = [
  "Let us now begin with the first question: Are you capable of starting fires",
  "Do you possess experience with armed and melee weapons",
  "How about construction? Know how to build to any extent",
  "Are you capable of reading maps",
  "Are you a seasoned rock climber",
  "Are you a particularly fit individual",
  "And, the last question: Can you hunt or fish"
]

#This stores responses to user interactions.
correctAnswerList = [
  "placeHolder"
  "Nice response! Alright, lets move on!",
  "Wow, that’s phenomenal! Next question.",
  "That’ll definitely come in handy!",
  "Whew! Now that’s insane!",
  "That is truly impressive!",
  "Yeah, that’s pretty useful!",
  "Foraging for food is quite useful.",
]

#This stores responses to user interactions.
incorrectAnswerList = [
  "placeHolder",
  "Aw dangit!",
  "Interesting. Let us move on.",
  "Err, maybe try looking at some maps at some time!",
  "Can’t get them all, am I right?",
  "Eesh, I wish you luck!",
  "Dang, couldn’t meet the mark!",
]
#This is a variable that stores a number indicative of a particular response within the correct answer list.
correctAnswerQuantified = 0

#This is a variable that stores a number indicative of a particular response within the incorrect answer list.
incorrectAnswerQuantified = 0

#This variable stores the score of the player.
scoreVar = 0

#This here ascertains that the user is provided a question after each response.
for question in questionList:
  userAnswerVar = input(question + "(Yes/No)?:")
#With each "yes" response, the user is awarded a point.
  if userAnswerVar.lower() == "yes":
    scoreVar = scoreVar + 1
    correctAnswerQuantified = correctAnswerQuantified + 1

    #This either breaks or continyes the string.
    if correctAnswerQuantified >= 7:
      break
    else:
      print(correctAnswerList[correctAnswerQuantified])

  elif userAnswerVar.lower() == "no":
    scoreVar = scoreVar + 0
    incorrectAnswerQuantified = incorrectAnswerQuantified + 1

    #This either breaks or continues the string.
    if incorrectAnswerQuantified >= 7:
      break
    else:
      print(incorrectAnswerList[incorrectAnswerQuantified])
      
#This is declared once the loop is exited.
print(f"You scored {scoreVar} points")

