from question_model import Question
from data import question_data
from quizBrain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)
xyz = QuizBrain(question_bank)
while(xyz.still_has_questions()):
    xyz.next_question()
print("Quiz ended")
print(f"You score {xyz.score}/{len(question_bank)}")
