import base64 
import tkinter as tk
from tkinter import ttk

def encode_url():
    url = entry.get()
    encoded_bytes = base64.b64encode(url.encode('utf-8'))
    encoded_url = encoded_bytes.decode('utf-8')
    encoded_entry.delete(0, tk.END)
    encoded_entry.insert(0, encoded_url)

def decode_url():
    encoded_url = entry.get()
    decoded_bytes = base64.b64decode(encoded_url.encode('utf-8'))
    decoded_url = decoded_bytes.decode('utf-8')
    output_var.set(decoded_url)

def paste_from_clipboard(event=None):
    clipboard_text = root.clipboard_get()
    entry.delete(0, tk.END)
    entry.insert(0, clipboard_text)

def copy_encoded_url():
    encoded_text = encoded_entry.get()
    root.clipboard_clear()
    root.clipboard_append(encoded_text)

def decrypt_url():
    encrypted_url = entry.get()
    decrypted_bytes = base64.b64decode(encrypted_url.encode('utf-8'))
    decrypted_url = decrypted_bytes.decode('utf-8')
    output_var.set(decrypted_url)

root = tk.Tk()
root.title("Base64 Encoder/Decoder")

# Get screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set window size to 80% of screen size
window_width = int(screen_width * 0.8)
window_height = int(screen_height * 0.8)
root.geometry(f"{window_width}x{window_height}")

frame = ttk.Frame(root, padding="20")
frame.grid(column=0, row=0, sticky=(tk.W + tk.E + tk.N + tk.S))  

title_label = ttk.Label(frame, text="Coded by anesboulf (anessersson)", font=("Helvetica", 20, "bold"))  
title_label.grid(column=0, row=0, columnspan=2, sticky=(tk.W + tk.E))  

label = ttk.Label(frame, text="Enter URL:", font=("Helvetica", 16))  
label.grid(column=0, row=1, sticky=tk.E)  

entry = ttk.Entry(frame, width=60, font=("Helvetica", 14))  
entry.grid(column=1, row=1, sticky=(tk.W + tk.E))  


style = ttk.Style()
style.configure('Custom.TButton', font=('Helvetica', 14))

encode_button = ttk.Button(frame, text="Encode", command=encode_url, width=20, style='Custom.TButton')  
encode_button.grid(column=0, row=2, sticky=tk.E)  

decode_button = ttk.Button(frame, text="Decode", command=decode_url, width=20, style='Custom.TButton')  
decode_button.grid(column=1, row=2, sticky=tk.W)  

encoded_entry = ttk.Entry(frame, width=60, font=("Helvetica", 14))  
encoded_entry.grid(column=1, row=3, sticky=(tk.W + tk.E))  

copy_button = ttk.Button(frame, text="Copy Encoded URL", command=copy_encoded_url, width=20, style='Custom.TButton')  
copy_button.grid(column=0, row=3, sticky=tk.E)  

output_var = tk.StringVar()
output_label = ttk.Label(frame, textvariable=output_var, wraplength=800, font=("Helvetica", 14))  
output_label.grid(column=0, row=4, columnspan=2, sticky=(tk.W + tk.E))  

entry.bind("<Control-v>", paste_from_clipboard)

root.columnconfigure(0, weight=1)  
root.rowconfigure(0, weight=1)    

root.mainloop()
