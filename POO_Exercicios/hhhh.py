import pandas as pd
def arquivo_validador(caminho):
    # presumi que talvez voces recebessem arquivos, com numeros de processos
    try:
        df = pd.read_csv(caminho, dtype={"coluna_cnj": "string"})
    except FileNotFoundError:
        return f"{caminho}.csv nao encontrado"
    except Exception as e:
        return "nao existe no documento"
    return df.dtypes

print(arquivo_validador('C:/Users/guilm/OneDrive/Documentos/teste.txt'))

