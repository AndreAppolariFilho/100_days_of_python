class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        user_input = input(f"Q.{self.question_number+1}: {self.question_list[self.question_number].text} (True/False)?")
        if self.check_answer(user_input, self.question_list[self.question_number].answer):
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was {self.question_list[self.question_number].answer}")
        print(f"Your current score is {self.score}/{self.question_number+1}")
        print("\n")
        self.question_number += 1

    def final_results(self):
        print("You've completed the quiz")
        print(f"Your final score was {self.score}/{self.question_number}")

    def check_answer(self, user_input, answer):
        return user_input.lower() == answer.lower()

