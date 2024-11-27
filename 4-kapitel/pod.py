import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO
from datetime import datetime
import requests

def save_image(img):
    current_date = datetime.now().strftime("%Y-%m-%d")
    filename = f"{current_date}_nasa.png"
    img.save(filename)
    print(f"Bild gespeichert als: {filename}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("NASA Bild des Tages")

    api_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
    response = requests.get(api_url)
    data = response.json()
    image_response = requests.get(data["url"])
    img = Image.open(BytesIO(image_response.content))
    img_scaled = img.resize((600, 400), Image.Resampling.LANCZOS)
    photo_image = ImageTk.PhotoImage(img_scaled)
    label_image = tk.Label(root, image=photo_image)
    label_image.pack()

    img_description = tk.Text(root, 
                              wrap="word", 
                              height=10)
    img_description.insert("1.0", data["explanation"])
    img_description.pack()

    save_button = tk.Button(root,
                            text="Bild speichern",
                            command=save_image(img))
    save_button.pack()

    root.mainloop()