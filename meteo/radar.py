import pandas as pd

# Pular as 8 linhas iniciais (metadados)
raw_df = pd.read_csv(
    "python/dados_A862_D_2008-03-21_2025-06-27.csv",
    sep=';',  # ou use sep=None + engine='python' como acima
    skiprows=9,
    encoding='latin1',
    header=None
)

# A primeira linha agora é o cabeçalho real
raw_df.columns = raw_df.iloc[0]
df = raw_df[1:].copy()

print(df.head())


#df1 = pd.read_csv("python/dados_A851_D_2007-06-05_2025-06-27.csv",  sep=';', on_bad_lines='skip', encoding='utf-8')
#print(df1.head())

#df2 = pd.read_csv("python/dados_A862_D_2008-03-21_2025-06-27.csv", sep=';', skiprows=8, encoding='latin1', #engine="python")
#print(df2.head(10))

#df3 = pd.read_csv("python/dados_A868_D_2010-06-23_2025-06-27.csv", on_bad_lines='skip')
#print(df3.head())