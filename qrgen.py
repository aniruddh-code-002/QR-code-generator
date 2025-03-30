import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

#Function to generate QR code
def generate_qr():
    data = entry.get()

    if not data:
        messagebox.showerror("Input Error", "Please enter a URL or text")
        return
    
    # Create a QR Code instance with dynamic sizing
    qr = qrcode.QRCode(
        version=None,  # Automatically determines the best version
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=8,  # Adjust box size for moderate scaling
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)  # Allow dynamic fitting

    # Create the QR code image and resize for consistent display
    img = qr.make_image(fill="black", back_color="white")
    img = img.resize((250, 250), Image.Resampling.LANCZOS)

    img.save("generated-qr.png")

    img_tk = ImageTk.PhotoImage(img)
    qr_label.config(image=img_tk)
    qr_label.image = img_tk

    messagebox.showinfo("QR-Code-Generated", "QR code has been generated and displayed!")

# Set up the Tkinter window
root = tk.Tk()
root.title("QR-Code-Generator")

#Create the input field and button
label = tk.Label(root, text="Enter URL or Text:")
label.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=20)

#Label to display the generated QR code image
qr_label = tk.Label(root)
qr_label.pack(pady=20)
root.mainloop()