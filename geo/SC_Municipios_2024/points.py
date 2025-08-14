import geopandas as gpd
from shapely.geometry import Point
import requests
from decimal import Decimal
import json
import time

# === CONFIG ===
geojson_path = "joinville_limite.geojson"
step = Decimal("0.01")  # você pode testar com 0.02 ou 0.005
tempo_entre_reqs = 0.5  # tempo entre requisições para não estourar rate limit
api_url = "https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&hourly=precipitation"

# === CARREGAR POLÍGONO ===
gdf = gpd.read_file(geojson_path)
poligono = gdf.unary_union  # transforma em único polígono

minx, miny, maxx, maxy = poligono.bounds

# === GERAÇÃO DOS PONTOS E VALIDAÇÃO ===
lat = Decimal(str(miny))
coordenadas_validas = []

print("🔍 Começando verificação de pontos...")

while lat <= Decimal(str(maxy)):
    lon = Decimal(str(minx))
    while lon <= Decimal(str(maxx)):
        ponto = Point(float(lon), float(lat))
        if poligono.contains(ponto):
            # Testa na API se esse ponto tem dados
            url = api_url.format(float(lat), float(lon))
            try:
                r = requests.get(url, timeout=10)
                if r.status_code == 200:
                    coordenadas_validas.append({
                        "lat": float(lat),
                        "lon": float(lon)
                    })
                    print(f"✅ {lat}, {lon} é válida")
                else:
                    print(f"⚠️  {lat}, {lon} retornou {r.status_code}")
            except Exception as e:
                print(f"❌ Erro em {lat}, {lon}: {e}")
            time.sleep(tempo_entre_reqs)
        lon += step
    lat += step

print(f"📝 Total de coordenadas válidas: {len(coordenadas_validas)}")

# === SALVAR EM JSON ===
with open("coordenadas_joinville_validas.json", "w") as f:
    json.dump(coordenadas_validas, f, indent=2)

print("📁 Arquivo salvo: coordenadas_joinville_validas.json")
