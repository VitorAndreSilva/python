from meteostat import Point, Daily
from datetime import datetime

location = Point(-26.3, -48.8)  # Joinville
start = datetime(2020, 1, 1)
end = datetime(2025, 6, 1)

data = Daily(location, start, end)
df = data.fetch()
print(df.head())