from geobr import read_neighborhood
import geopandas as gpd
import os

# Carrega todos os bairros do Brasil
bairros = read_neighborhood()

# Filtra apenas os bairros de Joinville (código IBGE: 4209102)
joinville = bairros[bairros['code_muni'] == 4209102]

# Renomeia coluna para facilitar
joinville = joinville[['name_neighborhood', 'geometry']]
joinville = joinville.rename(columns={'name_neighborhood': 'bairro'})

# Cria pasta para os arquivos
os.makedirs("geojson_bairros", exist_ok=True)

# Salva um arquivo .geojson por bairro
for _, row in joinville.iterrows():
    nome = row["bairro"].replace(" ", "_").lower()
    gdf_bairro = gpd.GeoDataFrame([row], crs=joinville.crs)
    gdf_bairro.to_file(f"geojson_bairros/{nome}.geojson", driver="GeoJSON")
