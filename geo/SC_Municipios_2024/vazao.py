from pyHydroWeb import download_hidroweb
import pandas as pd

def testar_estacao(cod_estacao, dt_inicial, dt_final):
    df = download_hidroweb(
        station=cod_estacao,
        dataType=3,         # 3 = vazão
        startDate=dt_inicial,
        endDate=dt_final,
        consistencyLevel=2, # dados consistidos
        path_folder=None    # sem salvar em disco
    )
    print(df.head())
    print("Total de linhas:", len(df))
    return df

# Exemplo de uso:
df_teste = testar_estacao(2648021, "2015-01-01", "2015-12-31")
