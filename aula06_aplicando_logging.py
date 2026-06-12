import pandas as pd
import logging

logging.basicConfig(filename='pipeline_test.log', encoding='utf-8', level= logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def ler_dados(arquivo1, arquivo2):
    try:
        df_alunos = pd.read_csv(arquivo1)
    except FileNotFoundError:
        logging.error("Arquivo de alunos não encontrado")
        exit()
    try:
        df_pagamentos = pd.read_csv(arquivo2)
    except FileNotFoundError:
        logging.error("Arquivo de pagamentos não encontrado")
        exit()
    return df_alunos, df_pagamentos

def transformar_dados(df_alunos, df_pagamentos):
    df_relatorio = pd.merge(df_alunos, df_pagamentos, on="id_aluno", how="left")
    return df_relatorio

def salvar_relatorio(df_relatorio, arquivo3):
    try:
        df_relatorio.to_csv(arquivo3, index=False)
    except OSError:
        logging.error("Erro ao salvar o relatório")
        exit()

def main():
    try:
        df_alunos, df_pagamentos = ler_dados("dados/alunos_ativos.csv", "dados/pagamentos.csv")
        logging.info("Leitura de dados finalizada")
        df_relatorio = transformar_dados(df_alunos, df_pagamentos)
        logging.info("Transformação realizada")
        salvar_relatorio(df_relatorio, "dados/relatorio_final_aula05.csv")
        logging.info("Processo concluído e salvo")
    except Exception as e:
        logging.error(f"Ocorreu um erro: {e}")
        exit()

if __name__ == "__main__":
    main()