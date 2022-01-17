class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(str(self.question_number) + ".) " + str(current_question.text) + " (True/False): ")
        self.check_answer(user_answer, current_question.answer)


    def questions_exist(self):
        return self.question_number < len(self.question_list)
    
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print("Wrong! The correct answer was " + str(correct_answer))
            
        print("Your current score is " + str(self.score) + "/" + str(self.question_number))
        
        
    def finished_quiz(self):
        print("\nYou've completed the quiz.\nYour final score was " + str(self.score) + "/" + str(self.question_number))