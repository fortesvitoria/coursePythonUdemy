from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

#create a list
question_bank = []

#loop getting the data from the list of dictionaries
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']

    #create an instance of the object
    new_quest = Question(question_text, question_answer)

    #append the object into a list
    question_bank.append(new_quest)

#Mostra texto e respostas dos dicionarios contidos nas listas
# for quest in question_bank:
#     print(quest.text, quest.answer)
    
quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

