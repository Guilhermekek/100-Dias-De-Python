# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


while True:
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
        print(output_list)
        break
    except KeyError:
        print("Voce colocou um numero")


# maneira que ela fez
# ela criou uma funçao para nao ter que fazer o loop com while
def generate_phoetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Voce colocou um numero")
        generate_phoetic()
    else:
        print(output_list)

generate_phoetic()