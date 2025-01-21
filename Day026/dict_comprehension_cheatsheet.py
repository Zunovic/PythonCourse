import random
import pandas

names =["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# {new_key:new_value for item in list}
students_scores = {student:random.randint(1, 100) for student in names}
print(students_scores)

# key:value for key:value in dictionary.items(), items ist wichtig damit wir die Namen + Scores bekommen
# aufgrund des Tuples
passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)

# Um auf alle Wörter des Strings zuzugreifen und die Anzahl der Buchstaben in einem dictionary zu speichern
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# key:value for key in sentence.split() Methode um alle Wörter voneinander zu trennen.
result = {word:len(word) for word in sentence.split()}
print(result)

# Wenn wir die Wochentage und die Temperatur in Fahrenheit konvertieren wollen
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# Die Formel für Fahrenheit ist (Temperatur in C x 9/5 + 32)
# new_key:new_value for key:value als tuple in dictionary.items() für die Werte als tuple
weather_f = {day:temp * 9 / 5 + 32 for (day, temp ) in weather_c.items()}
print(weather_f)



student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_frame = pandas.DataFrame(student_dict)
# In Pandas gibt es einen builtin loop for DataFrames.
# Mit dem kann man einfacher durch das Frame iterieren als mit
# einem normalen Loop.
for (index, row) in student_frame.iterrows():
    if row.student == "Angela":
        print(row.score)