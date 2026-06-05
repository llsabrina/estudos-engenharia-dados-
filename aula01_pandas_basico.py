import pandas as pd

alunos = {
    "id_aluno": [1, 2, 3, 4, 5, 6, 7],
    "nome": ["Ana Silva", "Bruno Lima", "Carla Souza", "Diego Matos", "Elena Costa", "Felipe Ramos", "Guilherme da Silva"],
    "curso":["Administração", "Direito", "Administração", "Medicina", "Direito", "Medicina", "Psicologia"],
    "status": ["Matriculado", "Cancelado", "Matriculado", "Rematrícula", "Matriculado", "Cancelado", "Matriculado"],
    "mensalidade": [850.00, 1200.00, 850.00, 3500.00, 1200.00, 3500.00, 2500.00]
}



df = pd.DataFrame(alunos)
print(df)

print("==" * 20)

print(df[(df["status"] == "Matriculado") & (df["mensalidade"] > 1000)]) 

print ("==" * 20)

print(df.sort_values("mensalidade", ascending=False))

print("==" * 20)

print(df.groupby("status")["mensalidade"].sum().sort_values(ascending=False))

pagamentos = {
    "id_pagamento": [1, 2, 3, 4, 5, 6, 7, 8],
    "id_aluno": [1, 2, 3, 4, 5, 6, 1, 3],
    "mes": ["Janeiro", "Janeiro", "Janeiro", "Janeiro", "Janeiro", "Janeiro", "Fevereiro", "Fevereiro"],
    "valor": [850.00, 1200.00, 850.00, 3500.00, 1200.00, 3500.00, 850.00, 850.00],
    "status_pagamento": ["Pago", "Atrasado", "Pago", "Pago", "Atrasado", "Pago", "Pago", "Atrasado"]
}

print("==" * 20)
df_pagamentos = pd.DataFrame(pagamentos)
print(df_pagamentos)

print(pd.merge(df, df_pagamentos, on="id_aluno", how="left"))

df_merged = pd.merge(df, df_pagamentos, on="id_aluno", how="left")

print("==" * 20)

print(df_merged[(df_merged["status_pagamento"] == "Atrasado")]) 
