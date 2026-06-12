# ✨ Estudos de Engenharia de Dados

Repositório de estudos práticos em Engenharia de Dados, construído do zero com foco em pipelines ETL reais.

Os dados simulam o contexto educacional: alunos matriculados, em rematrícula e cancelados, com suas respectivas tabelas de pagamento. Os DataFrames são mesclados para gerar relatórios completos por estudante, salvos em CSV ao final de cada pipeline.

---

## 💖 Tecnologias

- 🐍 Python 3.13
- 🐼 Pandas
- 📋 Logging (módulo nativo Python)
- 🗄️ MySQL Workbench

---

## 📊 Arquivos

| Arquivo | Conteúdo |
|---|---|
| `aula01_pandas_basico.py` | Criação de DataFrames, filtros com `&` e `\|`, ordenação e merge básico |
| `aula02_etl.py` | Leitura de CSVs, transformações e exportação do resultado |
| `aula03_funcoes.py` | Pipeline ETL organizado em funções reutilizáveis (`ler_dados`, `transformar_dados`, `salvar_relatorio`, `main`) |
| `aula04_try_except.py` | Tratamento de erros com `try/except` — `FileNotFoundError` e `OSError` |
| `aula05_pipeline_robusto.py` | Pipeline ETL completo com tratamento de erros integrado |
| `aula06_aplicando_logging.py` | Substituição dos `print()` por logging profissional com gravação em arquivo `.log` |

---

## 📁 Dados

- `alunos.csv` — base de alunos com status e mensalidade
- `pagamentos.csv` — histórico de pagamentos por aluno
- `alunos_ativos.csv` — alunos com status ativo filtrados
- `relatorio_final.csv` — resultado do merge entre alunos e pagamentos
- `relatorio_final_aula05.csv` — relatório gerado pelo pipeline robusto
- `pipeline_test.log` — log de execução do pipeline

---

## 🚀 Como rodar

1. 📦 Instale as dependências:
```bash
pip install pandas
```

2. ▶️ Execute o pipeline mais recente:
```bash
python aula06_aplicando_logging.py
```

3. 📋 Verifique o log gerado:
```bash
pipeline_test.log
```

---

## 📈 Progresso

- [x] Aula 01 — Pandas básico
- [x] Aula 02 — ETL com CSVs
- [x] Aula 03 — Funções e pipeline estruturado
- [x] Aula 04 — Tratamento de erros
- [x] Aula 05 — Pipeline robusto
- [x] Aula 06 — Logging profissional
- [ ] Aula 07 — Múltiplos arquivos e automação
- [ ] SQL avançado — CASE WHEN, CTEs, Window Functions
- [ ] Cloud — AWS ou GCP

---

## 👩‍💻 Autora

**Sabrina Alessandra Castro**  
Engenharia de Dados · em construção  
[github.com/llsabrina](https://github.com/llsabrina)