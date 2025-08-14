'''
import geopandas as gpd

# Substitua com o nome real do seu shapefile
gdf = gpd.read_file(r"C:\Users\ZETEC\Documents\VITOR\vscode\IFC\python\python\geo\SC_Municipios_2024\SC_Municipios_2024.shp")

# Filtra apenas Joinville (por nome)
joinville = gdf[gdf["NM_MUN"] == "Joinville"]  # ou a coluna que tiver o nome

# Salva como GeoJSON
joinville.to_file("joinville_limite.geojson", driver="GeoJSON")

print("✅ Arquivo GeoJSON de Joinville criado com sucesso!")
print(gdf.columns)     # mostra os nomes das colunas
print(gdf.head())      # mostra as primeiras linhas da tabela
'''

