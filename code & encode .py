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

frame = ttk.Frame(root, padding="20")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label = ttk.Label(frame, text="Enter URL:")
label.grid(column=0, row=0, sticky=tk.W)

entry = ttk.Entry(frame, width=40)
entry.grid(column=1, row=0)

encode_button = ttk.Button(frame, text="Encode", command=encode_url)
encode_button.grid(column=0, row=1)

decode_button = ttk.Button(frame, text="Decode", command=decode_url)
decode_button.grid(column=1, row=1)

encoded_entry = ttk.Entry(frame, width=40)
encoded_entry.grid(column=1, row=2)

copy_button = ttk.Button(frame, text="Copy Encoded URL", command=copy_encoded_url)
copy_button.grid(column=0, row=2)

output_var = tk.StringVar()
output_label = ttk.Label(frame, textvariable=output_var, wraplength=400)
output_label.grid(column=0, row=3, columnspan=2)

entry.bind("<Control-v>", paste_from_clipboard)

root.mainloop()
