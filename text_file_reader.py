import tkinter as tk
from tkinter import filedialog

def open_and_read_file():
    root = tk.Tk()
    root.withdraw()  

    file_path = filedialog.askopenfilename(
        title="Select a Text File",
        filetypes=[("Text Files", "*.txt")]
    )
    
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            print(f"Contents of {file_path}:\n")
            print(content)
    else:
        print("No file selected.")

if __name__ == "__main__":
    open_and_read_file()
