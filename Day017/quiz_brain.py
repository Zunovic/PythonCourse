

class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0


    def question_available(self):
        return self.question_number < len(self.question_list)


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        guess = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(guess, current_question.answer)


    def check_answer(self, guess, answer):
        if guess.lower() == answer.lower():
            self.score += 1
            print("Die Antwort ist richtig!\n")
        else:
            print("Falsche antwort!")
            print(f"Die richtige Antwort ist: {answer}\n")
        print(f"Du hast {self.score} von {self.question_number} richtig.")