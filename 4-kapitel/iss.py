import requests
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

def iss_location():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    if response.status_code == 200:
        data = response.json()
        iss_position = data["iss_position"]
        return iss_position
    return None

def iss_map():
    iss_position = iss_location()
    if iss_position:
        lon = float(iss_position["longitude"])
        lat = float(iss_position["latitude"])

        geo_map = Basemap(projection="ortho", lat_0=lat, lon_0=lon)
        geo_map.drawcoastlines()

        x, y = geo_map(lon, lat)
        geo_map.plot(x, y, "ro", markersize=10)

        plt.title("Aktuelle Position der ISS")
        plt.show()
    else:
        print("Fehler bei Abruf der ISS-Position.")

if __name__ == "__main__":
    iss_map()