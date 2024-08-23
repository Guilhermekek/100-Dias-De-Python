# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./input/Names/invited_names.txt") as file:
    nomes = file.read().splitlines()

with open("./input/Letters/starting_letter.txt", mode="r") as file:
    exemplo = file.read()
    print(exemplo)

for nome in nomes:
    with open(f"./Output/ReadyToSend/{nome}.txt", mode="w") as f:
        f.write(exemplo.replace("[name]",f"{nome}"))