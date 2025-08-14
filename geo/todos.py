import os
import json

# Caminho da pasta com os geojsons
PASTA_FIXTURES = "geojson_bairros/"
ARQUIVO_SAIDA = "bairros.geojson"

# Estrutura base de um GeoJSON unificado
geojson_unificado = {
    "type": "FeatureCollection",
    "features": []
}

# Percorre todos os arquivos da pasta
for nome_arquivo in os.listdir(PASTA_FIXTURES):
    if nome_arquivo.endswith(".geojson"):
        caminho_arquivo = os.path.join(PASTA_FIXTURES, nome_arquivo)
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            dados = json.load(f)
            if "features" in dados:
                geojson_unificado["features"].extend(dados["features"])

with open(ARQUIVO_SAIDA, "w", encoding="utf-8") as f:
    json.dump(geojson_unificado, f, ensure_ascii=False, indent=2)

print(f"GeoJSON unificado salvo em: {ARQUIVO_SAIDA}")
