# aprenderemos sobre try and exception

altura = float(input("Digite sua altura: "))
peso = int(input("Digite o seu peso: "))

if altura > 3:
    raise ValueError("Altura invalida")

bmi = peso/altura**2
print(bmi)


# desafio



# codigo
fruits = ["Apple", "Pear", "Orange"]

# Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    fruit = fruits[index]
    print(fruit + " pie")

make_pie(4)