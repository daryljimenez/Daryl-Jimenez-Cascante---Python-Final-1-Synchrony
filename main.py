# # (1) Generate question list, scores, and user answers
# question_list = [
#     {"question": "Let us now begin with the first question: Are you capable of starting fires?", "answer": "Yes"},
#     {"question": "What is the capital of France?", "answer": "Yes"},
#     # Add more questions here
# ]
# scores = 0
# user_answers = {}

# # (2) Introduction
# print("Hey, let me survey you on your ability to survive a zombie apocalypse with my questionaire!")

# # (3) (4) Display and answer questions
# for question in question_list:
#     print(question["question"])
#     user_answer = input("(Yes/No)").strip()
#     user_answers[question["question"]] = user_answer
#     if user_answer.lower() == question["answer"].lower():
#         scores += 1
#         print("Correct!\n")
#     else:
#         print(f"Sorry, the correct answer is {question['answer']}.\n")

# # (6) Check if the end of the list has been reached
# if len(question_list) == scores:
#     print("Congratulations! You've completed the quiz.")
# else:
#     print(f"Your score: {scores}/{len(question_list)}")
#     print("Thanks for playing. Better luck next time!")


print("Hey, let me survey you on your ability to survive a zombie apocalypse with my questionaire!")

#List, provides the program with the questions that are going to be asked throughout the execution of the program. 


questionList = [
  "Let us now begin with the first question: Are you capable of starting fires",
  "Do you possess experience with armed and melee weapons",
  "How about construction? Know how to build to any extent",
  "Are you capable of reading maps",
  "Are you a seasoned rock climber",
  "Are you a particularly fit individual",
  "And, the last question: Can you hunt or fish"
]

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

incorrectAnswerList = [
  "placeHolder",
  "Aw dangit!",
  "Interesting. Let us move on.",
  "Err, maybe try looking at some maps at some time!",
  "Can’t get them all, am I right?",
  "Eesh, I wish you luck!",
  "Dang, couldn’t meet the mark!",
]

correctAnswerQuantified = 0

incorrectAnswerQuantified = 0

scoreVar = 0

for question in questionList:
  userAnswerVar = input(question + "(Yes/No)?:")

  if userAnswerVar.lower() == "yes":
    scoreVar = scoreVar + 1
    correctAnswerQuantified = correctAnswerQuantified + 1
    
    if correctAnswerQuantified >= 7:
      break
    else:
      print(correctAnswerList[correctAnswerQuantified])

  elif userAnswerVar.lower() == "no":
    scoreVar = scoreVar + 0
    incorrectAnswerQuantified = incorrectAnswerQuantified + 1

    if incorrectAnswerQuantified >= 7:
      break
    else:
      print(incorrectAnswerList[incorrectAnswerQuantified])

print(f"You scored {scoreVar} points")

#questionListVar 

# #Daryl Jimenez-Cascante - Python Final 1 Synchrony

# #print("Hey! We're about to enter lockdown! Lets prepare for the incoming wave of the undead! Let's list out some living essentials for the new event! I'll provide you witha grade corresponding to the responses you provide! (Press any button)")

# #firstQuestion = input("Okay, now let's get started! What of the following is critical to surviving waves of zombies? Makeup (1), or Intercontinental ballistic missiles (2)? (1/2)")

# #if firstQuestion == ("1"):
#   #print("Nice response! Alright, lets move on!")
  
# #elif firstQuestion == ("2"):
#   #print("Wow! Real smart guy here! Let's go onto the next question.")

# #secondQuestion = input("If infected by a zombie, what next steps should you take to ")