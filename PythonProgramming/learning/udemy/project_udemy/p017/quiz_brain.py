class QuizBrain:
    def __init__(self, q_list):
        self.q_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_question(self):
        return self.q_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.q_number]
        self.q_number += 1
        user_answer = input(f'Q.{self.q_number}: {current_question.text} (True/False): ')
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        data_answer = user_answer.lower() == correct_answer.lower()
        if data_answer:
            self.score += 1
            print('You got it right!')
        else:
            print("That's wrong.")
        print(f'You answer was: {data_answer}')
        print(f'You score: {self.score}/{self.q_number}')

    def final_score(self):
        print('Game is Complete!')
        print(f'Your final score: {self.score}/{self.q_number}')