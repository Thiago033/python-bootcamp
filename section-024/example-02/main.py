#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

PLACEHOLDER = "[name]"

with open("section-024/example-02/Input/Names/invited_names.txt", "r") as name_list:
    names = name_list.readlines()

with open("section-024/example-02/Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()

for name in names:
    new_letter = letter_content.replace(PLACEHOLDER, name.strip())
    with open(f"section-024/example-02/Output/ReadyToSend/letter_for_{name.strip()}.txt", "w") as completed_letter:
        completed_letter.write(new_letter)
