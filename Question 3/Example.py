import threading
import tkinter as tk
import requests

def fetch_data():
    response = requests.get("https://httpbin.org/get")
    print(response.text)

def on_button_click():
    threading.Thread(target=fetch_data).start()

root = tk.Tk()
button = tk.Button(root, text="Fetch Data", command=on_button_click)
button.pack()

root.mainloop()


