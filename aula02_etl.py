import pandas as pd

df = pd.read_csv("dados/alunos.csv")

print(df)
print("==" * 20)

df_ativos = df[(df["status"] == "Matriculado") | (df["status"] == "Rematrícula")]
print(df_ativos)
print("==" * 20)

df_ativos.to_csv("dados/alunos_ativos.csv", index=False)

df_pagamentos = pd.read_csv("dados/pagamentos.csv")
print(df_pagamentos)
print("==" * 20)

df_relatorio= pd.merge(df_ativos, df_pagamentos, on="id_aluno", how ="left")
print(df_relatorio)
print("==" * 20)

df_relatorio.to_csv("dados/relatorio_pagamentos.csv", index=False)