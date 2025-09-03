class QuizBrain:

    def __init__(self, question_list):
        self.question_list = question_list
        self.question_num = 0
        self.score = 0

    def still_has_questions(self):
        return self.question_num < len(self.question_list)


    def next_question(self):
        current_ques = self.question_list[self.question_num]
        self.question_num += 1
        user_answer = input(f"Q.{self.question_num}. {current_ques.text} True/False?")
        self.check_answer(user_answer, current_ques.answer)


    def check_answer(self, user_answer, correct_ans ):
        if user_answer.lower() == correct_ans.lower():
            self.score += 1
            print("You got it right✅.")
        else:
            print("Wrong answer❌")

        print(f"Current Score: {self.score}/{len(self.question_list)}")
        print("\n")
