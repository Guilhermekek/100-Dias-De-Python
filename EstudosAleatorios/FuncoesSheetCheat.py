# aqui vou deixar algumas funçoes que sao importante e que ajudam muito e tambem alguns metodos
# lembrando que funçao quando chamada é autonoma, nao precisa de objeto nem classe
# metodo ja precisa

# funçao chamada dir(), quando usada ela retorna as funçoes que basicas que o python possui
print(dir(__builtins__))

# traz indormaçoes da fgunçao
print(help(max))

# retorna o tipo do item
print(type("lol"))

# retorna o valor maximo
a = [1,2,3,4,5]
print(max(a)) # retornou o maior valor da lista
print(max(2,9,86)) # retornou o maior valor dos nmeros passados pra ele

# separar
a = "lol-gosto-de-voce"
print(a.split("-"))
# podemos tambem passar quantas vezes no queremos que seja feita a separaçao
print(a.split("-",1))

# substituir
