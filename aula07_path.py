import logging
import pandas as pd
from pathlib import Path

logging.basicConfig(filename='pipeline_test.log', encoding='utf-8', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
try:
    vari = Path("C:/Users/sabri/Desktop/up level/python/dados/")

    save_relatorio = []

    for arquivo in vari.glob("*.csv"):
        df_alunos = pd.read_csv(arquivo)
        save_relatorio.append(df_alunos)

    pd.concat(save_relatorio).to_csv("C:/Users/sabri/Desktop/up level/python/dados/relatorio.csv", index=False)

    logging.info("Relatório gerado com sucesso.")
except Exception as e:
    logging.error(f"Ocorreu um erro: {e}")
    exit()