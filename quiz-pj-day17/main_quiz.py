from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for ques in question_data:
    ques_text= ques["text"]
    ques_answer = ques["answer"]
    new_q = Question(ques_text, ques_answer)
    question_bank.append(new_q)


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("You completed the quiz. Congrats!")
print(f"Your final score: {quiz.score}/{len(question_bank)} ")



