# Goal is to get the names from the txt file and get the text from the other txt file
# and putting both together to have a letter generated.

PERSON = "[name]"


with open("./Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PERSON, stripped_name)
        with open(f"./Letters/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)