import json
data ={"Amazon":{"senha":"Gui123","usuario":"admin"}}
with open('data.json', 'r') as f:
    json_data = json.load(f)
    if "Amazon" in json_data:
        print("existe")
        print(json_data["Amazon"])
    else:
        print("nao existe")