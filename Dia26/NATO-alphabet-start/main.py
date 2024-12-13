# Arquivo inicial do desafio do dia 26

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
dicionario = {}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
dados = pandas.read_csv("nato_phonetic_alphabet.csv")
for (index, row) in dados.iterrows():
    key = row.letter
    value = row.code
    dicionario[key] = value
print(dicionario)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
palavra = input("Coloque a sua palavra aqui:")
for i in palavra:
    for (key,value) in dicionario.items():
        if i.upper() == key:
            print(value)
