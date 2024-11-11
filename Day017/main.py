from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# Questions werden aus der Data.py gezogen und in der Liste "question_bank" gespeichert.
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.question_available():
    quiz.next_question()

print(f"Du hast alle Fragen beantwortet")
print(f"Von {quiz.question_number} Fragen hast du {quiz.score} richtige Antworten gegeben.")