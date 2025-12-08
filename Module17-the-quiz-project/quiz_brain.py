#TODO: asking the questions
#TODO: checking if the asnwer was correct
#TODO: checking if we're the end of the quiz

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    #Retrieve the item at the current question_number from the question_list. 
    #Use input() function to show the answer the Question text and ask for the user's answer
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        input(f"Q{self.question_number}: {current_question.text} (True/False):")

