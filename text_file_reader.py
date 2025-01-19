import tkinter as tk
from tkinter import filedialog

def open_and_read_file():
    """Opens a file dialog for selecting a text file and prints its contents."""
    root = tk.Tk()
    root.withdraw()  #

    file_path = filedialog.askopenfilename(
        title="Select a Text File",
        filetypes=[("Text Files", "*.txt")]
    )
    
    if file_path:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                print(f"Contents of {file_path}:\n")
                print(content)
        except Exception as e:
            print(f"Error reading file: {e}")
    else:
        print("No file selected.")

if __name__ == "__main__":
    open_and_read_file()

