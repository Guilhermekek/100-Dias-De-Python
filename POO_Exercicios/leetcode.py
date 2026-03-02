def twoSum(nums, target: int):
    valores = {}
    for i, num in enumerate(nums):
        complemento = target - num
        print(1)
        # Se o complemento já está no dicionário, significa que encontramos os dois valores
        if complemento in valores:
            print(2)
            # Retorna as posições (índices)
            return [valores[complemento], i]

        # Armazena o valor e sua posição no dicionário
        valores[num] = i

numero = [2,7,11,15]
print(twoSum(numero,9))