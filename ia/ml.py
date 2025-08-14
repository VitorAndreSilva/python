import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
arquivo = os.path.join(BASE_DIR, "clima_dias.csv")

# 1. Carregar dados
df = pd.read_csv(arquivo)  # colunas: data, bairro, precip, temp, umid, press, desastre(0/1)

# 2. Selecionar features climáticas
features = ["precip", "temp", "umid", "press"]
X = df[features].values

# 3. Padronizar
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Treinar Isolation Forest
clf = IsolationForest(contamination=0.005, random_state=42)
clf.fit(X_scaled)

# 5. Prever anomalias (-1 = anomalia, 1 = normal)
df["anomalia"] = clf.predict(X_scaled)
df["score"] = clf.decision_function(X_scaled)

# 6. Avaliar
anomalias_encontradas = df[df["anomalia"] == -1]
dias_com_desastre = df[df["desastre"] == 1]

intersecao = pd.merge(anomalias_encontradas, dias_com_desastre, on="data", how="inner")
print(f"Anomalias detectadas: {len(anomalias_encontradas)}")
print("Anomalias: ", anomalias_encontradas)
print(f"Dias de desastre que foram anomalias: {len(intersecao)}")
print("Estes foram os dias: ", intersecao)