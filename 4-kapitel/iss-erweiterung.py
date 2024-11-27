import requests
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import time

def iss_location():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    if response.status_code == 200:
        data = response.json()
        iss_position = data["iss_position"]
        return iss_position
    return None

def iss_map(minutes, positions):
    geo_map = Basemap(projection="ortho",lat_0=positions[0]["latitude"],lon_0=positions[0]["longitude"])
    geo_map.drawcoastlines()

    for position in positions:
        lon = float(position["longitude"])
        lat = float(position["latitude"])

        x, y = geo_map(lon, lat)
        geo_map.plot(x, y, "ro", markersize=5)
    
    plt.title(f"Verlauf der ISS-Position über {minutes} Minuten")
    plt.show()

if __name__ == "__main__":
    starttime = time.time()
    positions = []
    minutes = int(input("Wie viele Minuten soll die ISS getrackt werden? "))

    while time.time() - starttime < minutes * 60:
        position = iss_location()

        if position:
            positions.append(position)
        
        time.sleep(10)

    iss_map(minutes, positions)