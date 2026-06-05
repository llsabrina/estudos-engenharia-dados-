import pandas as pd

def carregar_alunos():
    try:
        df = pd.read_csv("dados/alunos.csv")
    except FileNotFoundError:
        print("Arquivo de alunos não encontrado")
        exit()
    return df


print(carregar_alunos())