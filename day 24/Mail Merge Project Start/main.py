PLACEHOLDER = "[name]"

with open("./input/Names/invited_names.txt") as names:
    name = names.readlines()
    print(name)

with open("./input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for n in name:
        stripped_n = n.strip()
        new_name = letter_content.replace(PLACEHOLDER, stripped_n)
        print(new_name)
        with open(f"./Output/ReadyToSend/Letter_for_{stripped_n}", mode="w") as new_letters:
            new_letter = new_letters.write(new_name)
