import pandas as pd

def ler_dados(arquivo1, arquivo2):
    df_alunos = pd.read_csv(arquivo1)
    df_pagamentos = pd.read_csv(arquivo2)

    return df_alunos, df_pagamentos

def transformar_dados(df_alunos, df_pagamentos):
    df_relatorio = pd.merge(df_alunos, df_pagamentos, on="id_aluno", how="left")
    return df_relatorio

def salvar_relatorio(df_relatorio, arquivo3):
    df_relatorio.to_csv(arquivo3, index=False)

def main():
    df_alunos, df_pagamentos = ler_dados("dados/alunos_ativos.csv", "dados/pagamentos.csv")
    print("leitura de dados finalizado")
    df_transformado = transformar_dados(df_alunos, df_pagamentos)
    print("transformação realizada")
    salvar_relatorio(df_transformado, "dados/relatorio_final.csv")
    print("processo concluido e salvo")

if __name__ == "__main__":
    main()