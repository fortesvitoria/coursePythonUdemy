#TODO: asking the questions
#TODO: checking if the asnwer was correct
#TODO: checking if we're the end of the quiz

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list #pass question_bank
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list) #return true or false

    #Retrieve the item at the current question_number from the question_list. 
    #Use input() function to show the answer the Question text and ask for the user's answer
    def next_question(self):
        current_question = self.question_list[self.question_number] #starts at 0, question_bank[0]
        self.question_number += 1 #adds 1, question_bank[1]
        user_answer = input(f"Q{self.question_number}: {current_question.text} (True/False):\n")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("Wrong answer!")
        
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.\n")