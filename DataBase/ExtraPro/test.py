import requests
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

def nasa():
    while True:
        url = "http://api.open-notify.org/iss-now.json"

        r = requests.get(url)

        Data = r.json()

        dt = Data['timestamp']

        lat = Data['iss_position']['latitude']

        lon = Data['iss_position']['longitude']

        print(f"Time And Date : {dt}")
        print(f"Latitude : {lat}")
        print(f"Longitude : {lon}")

        plt.figure(figsize=(10,8))

        ax = plt.axes(projection =ccrs.PlateCarree())

        ax.stock_img()

        plt.scatter(float(lon),float(lat),color = 'blue' , marker= 'o')

        plt.show()
nasa()