import json
import random
data ={"Amazon":{"senha":"Gui123","usuario":"admin"}}
with open('data.json', 'r') as f:
    json_data = json.load(f)
    if "Amazon" in json_data:
        print("existe")
        print(json_data["Amazon"])
    else:
        print("nao existe")

teste = {'French': 'partie', 'English': 'part'}, {'French': 'histoire', 'English': 'history'}, {'French': 'chercher', 'English': 'search'}, {'French': 'seulement', 'English': 'only'}

card = random.choice(teste)
print(card["French"])

# se ele acertou:
teste.remove(card)