from question_model import Question
from data import question_data, question_data_old
from quiz_brain import QuizBrain


question_bank = []

for q in question_data:
    # temp_q = Question(q["text"], q["answer"])
    temp_q = Question(q["question"], q["correct_answer"])
    question_bank.append(temp_q)
    
qb = QuizBrain(question_bank)

while qb.questions_exist():
    qb.next_question()

qb.finished_quiz()