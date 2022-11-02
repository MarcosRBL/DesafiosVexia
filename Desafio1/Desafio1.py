# Importação de bibliotecas
import pandas as pd
from datetime import datetime, date

# Função para calcular idade
def idade(nascimento):
    nascimento = datetime.strptime(nascimento, "%m/%d/%Y").date()
    diaAtual = date.today()
    return diaAtual.year - nascimento.year - ((diaAtual.month, diaAtual.day) < (nascimento.month, nascimento.day))

# Realiza leitura do JSON e transforma em um DataFrame
data = pd.read_json('data1.json')
df = pd.DataFrame(data)

# Utiliza o "dropna" para excluir as linhas que possuem algum valor nulo
df = df.dropna()

# Insere os valores de nascimento do DataFrame na função e cria uma coluna de idade
df['idade'] = df['nascimento'].apply(idade)

# Dropa as linhas que a idade seja menor que 30 anos
df = df.drop(df[df['idade'] < 30].index)

# Exporta todos os resultados do DataFrame para um XLSX
df.to_excel('desafio1.xlsx', index=False)