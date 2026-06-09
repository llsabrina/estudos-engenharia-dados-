import pandas as pd

def carregar_alunos():
    try:
        df_alunos = pd.read_csv("dados/alunos.csv")
    except FileNotFoundError:
        print("Arquivo de alunos não encontrado")
        exit()
    return df_alunos

def carregar_pagamentos():
    try:
        df_pagamentos = pd.read_csv("dados/pagamentos.csv")
    except FileNotFoundError:
        print("Arquivo de pagamentos não encontrado")
        exit()
    return df_pagamentos

def main():
    df_alunos = carregar_alunos()
    df_pagamentos = carregar_pagamentos()
    print(df_alunos)
    print(df_pagamentos)

if __name__ == "__main__":
    main()