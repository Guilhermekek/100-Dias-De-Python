import pandas as pd
import csv
#with open("weather_data.csv") as file:
    #data = file.readlines()
    #print(data)

#with open("weather_data.csv") as file:
    #data = csv.reader(file)
    #temperatures = []
    #for row in data:
        #if row[1] != "temp":
            #temperatures.append(int((row[1])))
    #print(temperatures)

# data = pd.read_csv('weather_data.csv')
#
# temperatura = data["temp"].to_list()
#
# media_temperatura = sum(temperatura)/len(temperatura)
# print(media_temperatura)

# essa foi a maneira normal de se fazer

# usando a biblioteca do pandas podemos fazer assim pra descobrir a media

# print(data["temp"].mean())

# resulta no mesmo resultado porem com menos linha de codigo

# pegar o valor maximo do data temperature

# print(data["temp"].max())

#pegadno o dadas de uma fileira
# print(data[data.day == "Monday"])
#  ela agora pediu para pegar o valor de quando a temperatura atingiu o maximo
# print(data[data.temp == data["temp"].max()])

# ela pediu para pegar a temperatura de Monday
# e converter para faranheit

# monday = data[data.day == "Monday"]
# x = (monday.temp * 9/5) + 32
# print(x)

# kkkkk deu certo
# achava que ia dar errado
# ela fez diferente

# como ela fez:
#monday = data[data.day == "Monday"]
#monday_temp = monday.temp[0]
#monday_temp_F = monday_temp * 9/5 + 32
#print(monday_temp_F)

# ela agora pediu para fazer um novo csv usando como base o csv de esquilos que ela passou
# esse novo csv  deve conter a cor dos esquilos e a quantidade
# farei do meu jeito sem pesquisar e usando conhecimentos antigos
# data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# print(data["Primary Fur Color"] == "Gray") # me retorna verdadeiro e falso
# #
# contador_g = 0
# contador_c = 0
# contador_b = 0
# for i in range(len(data["Primary Fur Color"])):
#     if data["Primary Fur Color"][i] == "Gray":
#         contador_g +=1
#     elif data["Primary Fur Color"][i] == "Cinnamon":
#         contador_c += 1
#     else:
#         contador_b += 1
# print(contador_g, contador_c, contador_b)
# data_dict = {"Fur Color":["Grey", "Cinammon", "Black"],
#              "Count":[contador_g, contador_c, contador_b]}
# data_frame = pd.DataFrame(data_dict)
# data_frame.to_csv("squirrel_count.csv")

# agora vamos para comoa professora fez

# import pandas
#
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
#
# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count],
# }
#
# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count_professora.csv")