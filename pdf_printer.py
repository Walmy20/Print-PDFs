import os
import tkinter as tk
from tkinter import filedialog, messagebox, Listbox, Scrollbar

# Global variable to keep track of the current folder
current_folder = ""

def select_folder():
    global current_folder
    # Open a file dialog to select a folder
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        current_folder = folder_selected  # Store the current folder
        pdf_files = list_pdfs_in_folder(folder_selected)
        update_listbox(pdf_files)

def list_pdfs_in_folder(folder):
    pdf_files = []
    # Walk through the directory and its subdirectories to find PDF files
    for dirpath, _, files in os.walk(folder):
        for file in files:
            if file.lower().endswith('.pdf'):
                pdf_files.append(os.path.join(dirpath, file))
    return pdf_files

def update_listbox(pdf_files):
    # Clear the current list in the listbox
    listbox.delete(0, tk.END)
    
    if not pdf_files:
        listbox.insert(tk.END, "No PDF files found in the selected folder or its subfolders.")
    else:
        for pdf_file in pdf_files:
            listbox.insert(tk.END, pdf_file)

def print_selected_pdfs():
    # Get the selected PDF files and print all others
    selected_indices = listbox.curselection()
    selected_files = []

    # Get the paths of the selected PDFs
    for index in selected_indices:
        selected_file = listbox.get(index)
        selected_files.append(selected_file)

    # Print all PDFs in the list except the selected ones
    pdf_files = listbox.get(0, tk.END)
    for pdf_path in pdf_files:
        if pdf_path not in selected_files:
            print_pdf(pdf_path)

def print_pdf(pdf_path):
    # Using the os command to print the PDF
    try:
        if os.name == 'nt':  # For Windows
            os.startfile(pdf_path, "print")
        else:  # For Unix-based systems
            os.system(f'lpr "{pdf_path}"')
        print(f"Sent {pdf_path} to printer.")
    except Exception as e:
        print(f"Failed to print {pdf_path}: {e}")

# Setting up the Tkinter GUI
root = tk.Tk()
root.title("PDF Printer")
root.geometry("500x400")

# Create a button to select the folder
btn_select_folder = tk.Button(root, text="Select Folder", command=select_folder)
btn_select_folder.pack(pady=10)

# Create a listbox to display PDF files
listbox = Listbox(root, selectmode=tk.MULTIPLE, width=70, height=15)  # Allow multiple selection
listbox.pack(pady=10)

# Create a scrollbar for the listbox
scrollbar = Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Create a button to print all PDFs except the selected ones
btn_print_selected = tk.Button(root, text="Print PDFs", command=print_selected_pdfs)
btn_print_selected.pack(pady=10)

# Start the main event loop
root.mainloop()

