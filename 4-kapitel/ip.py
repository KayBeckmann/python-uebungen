import tkinter as tk
import requests, webbrowser, folium

def get_ip_adresse():
    try:
        response = requests.get("https://api.ipify.org/")
        return response.text
    except requests.exceptions.RequestException:
        return "Deine IP -Adresse konnte nicht ermittelt werden."

def get_ip_location(ip_address):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        data = response.json()
        return (data["lat"], data["lon"])
    except requests.exceptions.RequestException:
        return None

def show_location_on_map(location):
    map = folium.Map(location=location,
                     zoom_start=12)
    folium.Marker(location).add_to(map)
    map_path="iplocation.html"
    map.save(map_path)
    webbrowser.open(map_path)

def show_ip_and_location():
    ip_address = get_ip_adresse()
    location = get_ip_location(ip_address)
    if location:
        show_location_on_map(location)
    ip_label.config(text=f"IP-Adresse: {ip_address}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Wo bin ich?")
    root.geometry("600x400")

    ip_label_font = ("Arial", 16, "bold")
    button_font = ("Arial", 16)

    ip_label = tk.Label(root,
                        text="...",
                        bg="yellow",
                        font=ip_label_font)
    ip_label.pack(padx=20,
                  pady=20,
                  fill=tk.BOTH,
                  expand=True)
    
    tk.Button(root,
              text="Standort ermitteln",
              command=show_ip_and_location,
              font=button_font,
              height=2,
              width=20).pack(pady=20)

    root.mainloop()

# https://api.ipify.org/ -> IP-Adresse
# http://ip-api.com/json/84.153.149.202 -> Informationen